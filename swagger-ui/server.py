#!/usr/bin/env python3
"""
Swagger UIを提供するためのシンプルなHTTPサーバー
"""
import http.server
import socketserver

PORT = 8081
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Swagger UIサーバーが http://localhost:{PORT} で起動しました")
    httpd.serve_forever()
