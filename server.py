#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Serve this directory over HTTP for local testing."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8081,
        help="Port to listen on (default: 8081).",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    handler = http.server.SimpleHTTPRequestHandler

    with ReusableTCPServer(("", args.port), handler) as httpd:
        print(f"Serving {root} at http://localhost:{args.port}/")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
