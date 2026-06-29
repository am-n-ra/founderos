import asyncio, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from FounderOS.Runtime.engine.fhq_daemon import run_http, FHQDaemon
asyncio.run(run_http(FHQDaemon(), port=8743))
