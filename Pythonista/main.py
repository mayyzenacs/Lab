from http.server import HTTPServer, BaseHTTPRequestHandler

server = HTTPServer(("localhost", 8000), BaseHTTPRequestHandler)