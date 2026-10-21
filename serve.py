"""Static file server for url.peka.ai.id (microlink page).

Serves this directory on 127.0.0.1:8086. Reached publicly through the
reverse SSH tunnel (server port 18089) and the Caddy vhost for
url.peka.ai.id on 43.156.63.114.
"""
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = 8086


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "public, max-age=300")
        super().end_headers()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
