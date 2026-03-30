from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/plate-capture', methods=['POST'])
def receive_plate():
    data = request.json
    print(f"\n[!] ALERT: Incoming IoT Transmission Captured!")
    print(f"    Camera ID: {data.get('camera_id')}")
    print(f"    License Plate: {data.get('plate_number')}")
    print(f"    AI Confidence: {data.get('confidence')}%")
    return jsonify({"status": "success", "message": "Data logged."}), 200

if __name__ == '__main__':
    print("[*] ALPR Backend Server listening on port 80...")
    # Listens on all interfaces so the Ubuntu VM can reach it
    app.run(host='0.0.0.0', port=80)