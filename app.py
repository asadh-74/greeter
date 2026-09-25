#!/usr/bin/env python3
"""Tiny greeter web app for the 'Ship a Containerized App with Git & Docker' exercise."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date
import os

NAME = "Asad Hussain"
PORT = int(os.environ.get("PORT", 8080))

GREETING_HTML = f"""
<html>
  <head><title>Greeter</title></head>
  <body style="font-family: sans-serif; text-align: center; margin-top: 50px;">
    <h1>Hello there, my name is {NAME}!</h1>
        <p>"Stay hungry, stay foolish."</p>
    <p>Serving from inside a Docker container.</p>
  </body>
</html>
"""


class GreeterHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(GREETING_HTML.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), GreeterHandler)
    print(f"Greeter running on port {PORT} ...")
    server.serve_forever()
