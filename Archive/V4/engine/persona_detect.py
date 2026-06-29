"""
Persona detection engine for FounderHQ.
Reads user messages, detects persona from keywords/patterns,
updates CURRENT_STATE.md and writes _PERSONA_STATE.md.

Usage:
    python persona_detect.py "user message text"
    echo "user message text" | python persona_detect.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATE_DIR = BASE_DIR / "State"
CONCEPTS_DIR = BASE_DIR / "concepts"

DETECTION_MATRIX = {
    "CTO": {
        "strong": ["api", "code", "deploy", "docker", "microservice", "algorithme", "frontend", "backend", "git", "bug"],
        "medium": ["architecture", "infrastructure", "server", "scalable", "deploiement", "base de donnees", "compute", "stack", "model", "technical debt"],
        "patterns": [r"\b(cto|tech|dev|engineering|technique|developpeur|programmation)\b"],
        "strong_weight": 0.15,
        "medium_weight": 0.08
    },
    "CFO": {
        "strong": ["cash", "roi", "fundraising", "grant", "investor", "bailleur", "subvention", "tresorerie", "burn rate", "investissement"],
        "medium": ["cost", "budget", "revenue", "margin", "price", "runway", "fonds", "financement", "profit", "cout", "argent", "depense"],
        "patterns": [r"\b(cfo|finance|financial|money|financier|investisseur|capital)\b"],
        "strong_weight": 0.15,
        "medium_weight": 0.08
    },
    "COO": {
        "strong": ["deadline", "sprint", "workflow", "ressource", "capacite", "echeance", "tache", "pipeline", "blocker", "gantt"],
        "medium": ["schedule", "timeline", "priority", "operations", "organize", "planning", "processus", "flux", "gestion", "chantier"],
        "patterns": [r"\b(coo|operational|ops|planning|operationnel|organisation)\b"],
        "strong_weight": 0.15,
        "medium_weight": 0.08
    },
    "Mentor": {
        "strong": ["youtube", "tiktok", "tutoriel", "apprendre", "enseigner", "accompagner", "audience", "communaute", "engagement", "contenu"],
        "medium": ["content", "community", "teach", "learn", "growth", "share", "help", "video", "post", "education", "guide", "formation"],
        "patterns": [r"\b(mentor|coach|teaching|learning|accompagnement|formation|pedagogie)\b"],
        "strong_weight": 0.15,
        "medium_weight": 0.08
    },
    "Strategist": {
        "strong": ["vision", "mission", "impact", "innovation", "ecosysteme", "positionnement", "long terme", "partenariat", "croissance"],
        "medium": ["strategy", "market", "future", "partnership", "why", "marche", "direction", "positioning"],
        "patterns": [r"\b(strateg|vision|mission|direction|strategique|visee)\b"],
        "strong_weight": 0.15,
        "medium_weight": 0.08
    },
}

EXPLICIT_TRIGGERS = {
    "switch to cto": "CTO", "as cto": "CTO", "in cto mode": "CTO", "cto hat": "CTO",
    "switch to cfo": "CFO", "as cfo": "CFO", "in cfo mode": "CFO", "cfo hat": "CFO",
    "switch to coo": "COO", "as coo": "COO", "in coo mode": "COO", "coo hat": "COO",
    "switch to mentor": "Mentor", "as mentor": "Mentor", "in mentor mode": "Mentor", "mentor hat": "Mentor",
    "switch to strategist": "Strategist", "as strategist": "Strategist", "in strategist mode": "Strategist", "strategist hat": "Strategist",
    "back to default": "Strategist", "reset persona": "Strategist", "default mode": "Strategist",
}

VENTURE_TRIGGERS = [
    "i have an idea",
    "j'ai une idee",
    "new venture",
    "nouveau projet",
    "new business",
    "nouvelle entreprise",
    "start a new",
    "create a new",
    "i want to build",
    "je veux creer",
    "je veux lancer",
]

THRESHOLD = 0.08


def rp(path):
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def detect_persona(user_message: str) -> dict:
    """Detect persona from message.
    Returns {persona: str, confidence: float, trigger_venture: bool}"""
    msg_lower = user_message.lower()

    # 1. Explicit triggers (direct persona switch commands)
    for trigger, persona in EXPLICIT_TRIGGERS.items():
        if trigger in msg_lower:
            return {"persona": persona, "confidence": 1.0, "trigger_venture": False}

    # 2. Venture trigger detection — "I have an idea" forces Strategist + VAOS
    for vt in VENTURE_TRIGGERS:
        if vt in msg_lower:
            return {"persona": "Strategist", "confidence": 0.8, "trigger_venture": True}

    # 3. Tiered keyword + pattern scoring
    scores = {}
    for persona, config in DETECTION_MATRIX.items():
        strong_kws = config.get("strong", [])
        medium_kws = config.get("medium", [])
        patterns = config["patterns"]
        sw = config.get("strong_weight", 0.12)
        mw = config.get("medium_weight", 0.06)

        strong_matches = sum(1 for kw in strong_kws if kw.lower() in msg_lower)
        medium_matches = sum(1 for kw in medium_kws if kw.lower() in msg_lower)
        pattern_matches = sum(1 for p in patterns if re.search(p, msg_lower, re.IGNORECASE))

        score = round(strong_matches * sw + medium_matches * mw + pattern_matches * 0.2, 4)
        scores[persona] = score

    # Find highest scored persona
    best_persona = max(scores, key=lambda p: scores[p])
    best_score = scores[best_persona]

    if best_score >= THRESHOLD:
        return {"persona": best_persona, "confidence": round(min(best_score, 1.0), 3), "trigger_venture": False}

    # No clear winner — return current persona (no change)
    cs = rp(STATE_DIR / "CURRENT_STATE.md")
    current_persona = "Strategist"
    m = re.search(r"\*\*Active Persona:\*\*\s*(.+)", cs)
    if m:
        current_persona = m.group(1).strip()
    if current_persona == "DEFAULT" or not current_persona:
        current_persona = "Strategist"
    return {"persona": current_persona, "confidence": 0.0, "trigger_venture": False}


def update_active_persona(persona: str) -> bool:
    """Update CURRENT_STATE.md Active Persona field. Returns True if changed."""
    cs_path = STATE_DIR / "CURRENT_STATE.md"
    if not cs_path.exists():
        return False
    cs = cs_path.read_text(encoding="utf-8", errors="replace")

    pattern = r"(\*\*Active Persona:\*\*)\s*(.+)"
    m = re.search(pattern, cs)
    if not m:
        return False

    current = m.group(2).strip()
    if current == persona:
        return False

    new_cs = re.sub(pattern, rf"\1 {persona}", cs)
    cs_path.write_text(new_cs, encoding="utf-8")
    return True


def write_persona_state(persona: str, confidence: float, trigger_venture: bool = False, novice_mode: bool = False, frameworks: list = None) -> None:
    """Write _PERSONA_STATE.md with current persona info."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    frameworks_str = ", ".join(frameworks) if frameworks else "none"
    content = f"""# PERSONA STATE
**Detected:** {persona}
**Confidence:** {confidence}
**Trigger Venture:** {str(trigger_venture)}
**Novice Mode:** {str(novice_mode)}
**Last Updated:** {now} Lome UTC+0
## Frameworks to Load
{frameworks_str}
"""
    (STATE_DIR / "_PERSONA_STATE.md").write_text(content, encoding="utf-8")


def check_novice_mode() -> bool:
    """Check if PROFILE.md has Capability Level = novice."""
    profile = rp(CONCEPTS_DIR / "PROFILE.md")
    if not profile:
        return False
    m = re.search(r"\*\*Capability Level:\*\*\s*(.+)", profile)
    if m:
        return m.group(1).strip().lower() == "novice"
    return False


def get_frameworks_for_persona(persona: str) -> list:
    """Read persona file and extract 'Frameworks to Preload' section.
    Returns list of framework file paths relative to BASE_DIR."""
    persona_path = BASE_DIR / "Personas" / f"{persona}.md"
    if not persona_path.exists():
        return []
    text = persona_path.read_text(encoding="utf-8", errors="replace")
    frameworks = []
    in_section = False
    for line in text.splitlines():
        if "## Frameworks to Preload" in line:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.strip().startswith("- ") and "**" in line:
            m = re.search(r"\*\*([A-Z_]+)\*\*", line)
            if m:
                frameworks.append(m.group(1))
    return frameworks


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

    if len(sys.argv) >= 2:
        user_message = sys.argv[1]
    else:
        user_message = sys.stdin.read().strip()
        if not user_message:
            print(json.dumps({"error": "No message provided. Usage: python persona_detect.py 'message'"}, ensure_ascii=False))
            sys.exit(1)

    result = detect_persona(user_message)
    changed = update_active_persona(result["persona"])
    novice = check_novice_mode()
    frameworks = get_frameworks_for_persona(result["persona"])
    write_persona_state(result["persona"], result["confidence"], result["trigger_venture"], novice, frameworks)

    result["changed"] = changed
    result["novice_mode"] = novice
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
