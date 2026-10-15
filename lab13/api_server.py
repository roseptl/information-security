
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class LogHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/logs":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        data = json.loads(body.decode("utf-8"))

        with open("received_log.txt", "a", encoding="utf-8") as file:
            file.write(data["log"])
            file.write("\n")

        response = json.dumps({
            "status": "success",
            "message": "Test log received"
        }).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

        print("Test log received and saved")


server = HTTPServer(("127.0.0.1", 8000), LogHandler)

print("API server is running at http://127.0.0.1:8000")
server.serve_forever()
