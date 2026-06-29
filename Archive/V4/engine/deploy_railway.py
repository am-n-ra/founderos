"""Generate Railway deployment config for FounderHQ daemon.

Usage:
  python deploy_railway.py
  This prints the configuration. Follow instructions to deploy.

Railway auto-sets the $PORT environment variable.
The daemon reads it and binds to that port.
"""

import json

RAILWAY_CONFIG = {
    "build": {
        "builder": "NIXPACKS",
        "buildCommand": (
            "pip install -r FounderOS/Runtime/engine/requirements-daemon.txt"
        ),
    },
    "deploy": {
        "startCommand": (
            "python FounderOS/Runtime/engine/fhq_daemon.py "
            "--mode http --port $PORT"
        ),
        "healthcheckPath": "/health",
        "restartPolicyType": "ON_FAILURE",
    },
}

RAILWAY_NIXPACKS = """# .buildpacks (optional -- Railway auto-detects Python)
# Not needed if using NIXPACKS builder (default)
"""

DEPLOY_STEPS = """
=== Deploy FounderHQ to Railway ===

Prerequisites:
  - Railway account (free tier available)
  - Railway CLI installed: npm i -g @railway/cli

Step 1: Initialize
  cd FounderHQ
  railway login
  railway init

Step 2: Create railway.json
  Run: python deploy_railway.py > railway.json
  Or copy the JSON block below to railway.json

Step 3: Add environment variables (optional)
  railway variables --set FHQ_GIST_TOKEN=your_token

Step 4: Deploy
  railway up

Step 5: Get URL
  railway domain
  # -> https://founderhq-production.up.railway.app

Step 6: Verify
  curl https://your-app.up.railway.app/health

Step 7: Connect Claude
  Claude.ai -> Settings -> Connectors -> Add custom connector
  URL: https://your-app.up.railway.app/mcp

=== railway.json ===
"""


if __name__ == "__main__":
    print(DEPLOY_STEPS)
    print(json.dumps(RAILWAY_CONFIG, indent=2))
    print()
    print("=== Deploy command ===")
    print("railway up")
