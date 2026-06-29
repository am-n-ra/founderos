"""Interactive script to deploy FounderHQ daemon to PythonAnywhere.

Usage:
  python deploy_pythonanywhere.py --username your-pa-username

This script prints instructions. PythonAnywhere supports ASGI (FastAPI)
via its web tab, which is compatible with fhq_daemon.py HTTP mode.
"""

import argparse

PA_WSGI_TEMPLATE = '''
import sys
import asyncio

# Add project to path
path = "/home/{username}/FounderHQ"
if path not in sys.path:
    sys.path.insert(0, path)

# Import the daemon
from FounderOS.Runtime.engine.fhq_daemon import create_http_app, FHQDaemon

# Initialize daemon and run first cycle
daemon = FHQDaemon()
daemon._mode = "http"
loop = asyncio.get_event_loop()
loop.run_until_complete(
    asyncio.get_running_loop().run_in_executor(None, daemon.run_cycle)
)

# Start background cycle loop
loop.create_task(daemon.cycle_loop())

# FastAPI app for PythonAnywhere WSGI
app = create_http_app(daemon)
'''

DEPLOY_STEPS = """
=== Deploy FounderHQ to PythonAnywhere ===

Step 1: Upload files
  - Open a bash console on PythonAnywhere
  - Run: git clone https://github.com/YOUR_REPO/FounderHQ.git
  - Or upload manually via the Files tab

Step 2: Install dependencies
  - Open a bash console
  - Run: pip install --user -r FounderOS/Runtime/engine/requirements-daemon.txt

Step 3: Set up web app
  - Go to Web tab
  - Click "Add a new web app"
  - Choose "Manual Configuration"
  - Choose Python 3.10+
  - Note your domain: https://YOUR_USERNAME.pythonanywhere.com

Step 4: Configure WSGI
  - In the Web tab, click on the WSGI configuration file link
  - Replace the entire content with the WSGI template below
  - Replace {username} with your actual PythonAnywhere username

Step 5: Set working directory
  - In the Web tab, set working directory to: /home/{username}/FounderHQ

Step 6: Reload
  - Click "Reload" button in the Web tab

Step 7: Verify
  - Visit: https://{username}.pythonanywhere.com/health
  - Expected: {{"status":"alive","cycle":1,...}}

Step 8: Connect Claude
  - Go to Claude.ai -> Settings -> Connectors -> Add custom connector
  - Enter: https://{username}.pythonanywhere.com/mcp
  - Claude will discover 7 tools

=== WSGI Template (paste into PythonAnywhere WSGI file) ===
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate PythonAnywhere deploy instructions for FounderHQ"
    )
    parser.add_argument(
        "--username", required=True,
        help="Your PythonAnywhere username"
    )
    args = parser.parse_args()

    print(DEPLOY_STEPS.format(username=args.username))
    print(PA_WSGI_TEMPLATE.format(username=args.username))
    print()
    print(f"After deploying, your MCP endpoint will be:")
    print(f"  https://{args.username}.pythonanywhere.com/mcp")
    print()
    print(f"Health check:")
    print(f"  https://{args.username}.pythonanywhere.com/health")
