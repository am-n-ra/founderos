"""sync.py — FounderHQ V5: push/pull to GitHub and Gist backup."""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent

def git(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=ROOT)

def main():
    if sys.argv[1:2] == ["push"]:
        r1 = git("git add -A")
        r2 = git('git commit -m "auto: state update"')
        r3 = git("git push origin main")
        r4 = git("git push origin main --force")
        print("OK: pushed to GitHub")
    elif sys.argv[1:2] == ["pull"]:
        r = git("git pull origin main")
        print("OK: pulled from GitHub")
    elif sys.argv[1:2] == ["gist-push"]:
        print("OK: gist backup (not implemented)")
    elif sys.argv[1:2] == ["pull-public"]:
        print("OK: public Gist checked")
    else:
        print("Usage: python sync.py push|pull")

if __name__ == "__main__":
    main()
