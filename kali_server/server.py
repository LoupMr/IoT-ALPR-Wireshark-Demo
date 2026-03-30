from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Only listen for our specific API path
        if self.path == '/api/v1/plate-capture':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                # Parse the JSON from the Ubuntu Camera
                data = json.loads(post_data.decode('utf-8'))
                print(f"\n[!] ALERT: Incoming IoT Transmission Captured!")
                print(f"    Camera ID: {data.get('camera_id')}")
                print(f"    License Plate: {data.get('plate_number')}")
                print(f"    AI Confidence: {data.get('confidence')}%")

                # Send a success response back
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"status": "success", "message": "Data logged."}')
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    # This stops Python from printing standard web logs so we only see the alerts
    def log_message(self, format, *args):
        return 

if __name__ == '__main__':
    # Listen on all network interfaces on port 80
    server_address = ('0.0.0.0', 80)
    httpd = HTTPServer(server_address, RequestHandler)
    print("[*] ALPR Backend Server listening on port 80...")
    print("[*] Waiting for unencrypted IoT transmissions...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Server shutting down.")
        httpd.server_close()