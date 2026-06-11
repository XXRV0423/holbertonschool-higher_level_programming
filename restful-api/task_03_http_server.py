import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self._respond(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._respond(200, "application/json", json.dumps(payload))
        elif self.path == "/status":
            self._respond(200, "text/plain", "OK")
        elif self.path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            self._respond(200, "application/json", json.dumps(payload))
        else:
            self._respond(404, "text/plain", "Endpoint not found")


    def _respond(self, status_code, content_type, body):
            self.send_response(status_code)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(body.encode("utf-8"))
    def log_message(self, format, *args):
        print(f"[{self.address_string()}] {format % args}")

if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), SimpleAPIHandler)
    print("Server running on port 8000...")
    server.serve_forever()
