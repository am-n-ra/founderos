# Project Template — Canonical Folder Structure

Every project under `projects/<PROJECT>/` MUST conform to this structure.

## Directory Layout

```
projects/<PROJECT>/
├── README.md              # Project overview, status, mission, key links
├── STRATEGY.md            # Strategic positioning, goals, milestones
├── KNOWLEDGE.md           # Domain-specific knowledge accumulated
├── ACCOUNTS.md            # Accounts, credentials (reference only, no secrets)
├── ASSETS/                # Logos, media, design files
├── docs/                  # Project-specific documentation
└── CODE/                  # Git submodule reference
    └── README.md          # Points to GitHub repo, describes submodule setup
```

## Status Badges

| Badge | Phase | Description |
|-------|-------|-------------|
| 🟢 **IDEA** | Idea | Concept stage, no active work |
| 🟡 **VALIDATION** | Validation | Active testing, market validation |
| 🔵 **LAUNCH** | Launch | Public launch, early traction |
| 🟣 **GROWTH** | Growth | Scaling, revenue generation |
| ⚪ **MATURE** | Mature | Stable, self-sustaining |

## Rules

1. **All code MUST be in `CODE/` as a git submodule.** Never inline code in the project folder. The `CODE/README.md` must point to the GitHub repo and include the `git submodule add` command.
2. **No secrets in ACCOUNTS.md.** Reference account types and platforms only. Actual credentials go in `.env` or a password manager.
3. **ASSETS/ is for binary media.** Logos, screenshots, mockups, design files. Keep it under 10MB per project.
4. **docs/ is for documentation.** Manuals, guides, research, references.
5. **README.md is the entry point.** Every folder must have a README.md that explains its purpose.

## README Template

```markdown
# <PROJECT NAME>

**Status:** `IDEA` / `VALIDATION` / `LAUNCH` / `GROWTH` / `MATURE`

## Mission

One-line mission statement.

## Key Links

| Link | URL |
|------|-----|
| GitHub | https://github.com/... |
| Live | https://... |
| Docs | ./docs/ |

## Current Phase

What is happening right now.

## Blockers

- Blocker 1
- Blocker 2

## Quick Reference

| Document | Location |
|----------|----------|
| Strategy | ./STRATEGY.md |
| Knowledge | ./KNOWLEDGE.md |
| Accounts | ./ACCOUNTS.md |
| Assets | ./ASSETS/ |
| Code | ./CODE/ |
```

## Adding a Git Submodule

```bash
# From the project root:
git submodule add https://github.com/<user>/<repo>.git CODE/<repo-name>

# Or for an existing project:
cd projects/<PROJECT>
git submodule add https://github.com/<user>/<repo>.git CODE/<repo-name>
```

## Repository Setup Checklist

When creating a new GitHub repo for a project, run through this checklist:

```markdown
- [ ] Create GitHub repo (public or private) under `am-n-ra/<project-name>`
- [ ] Add initial README matching project README
- [ ] Add CODEOWNERS
- [ ] Configure branch protection (require PR review)
- [ ] Run: git submodule add <url> FounderOS/projects/<PROJECT>/CODE/<repo-name>
- [ ] Update PROJECTS_MASTER_INDEX.md with repo URL and submodule status
- [ ] Update CODE/README.md with submodule status ✅
```

## Footer

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | 2026-06-27 |
| Owner | FounderOS Protocols |
