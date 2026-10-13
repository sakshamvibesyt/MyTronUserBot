import os
import sys
import signal
import threading
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"MyTronUserBot is running")

    def log_message(self, format, *args):
        pass


port = int(os.environ.get("PORT", "10000"))

server = ThreadingHTTPServer(("0.0.0.0", port), HealthHandler)

threading.Thread(
    target=server.serve_forever,
    daemon=True
).start()

print(f"HTTP health server listening on port {port}", flush=True)

bot = subprocess.Popen(
    [sys.executable, "-u", "-m", "main"]
)


def shutdown(signum, frame):
    print("Stopping MyTronUserBot...", flush=True)

    if bot.poll() is None:
        bot.terminate()

    threading.Thread(
        target=server.shutdown,
        daemon=True
    ).start()


signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)

try:
    exit_code = bot.wait()
finally:
    server.shutdown()
    server.server_close()

sys.exit(exit_code)
