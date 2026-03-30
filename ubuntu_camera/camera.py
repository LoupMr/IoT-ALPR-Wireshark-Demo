import time
import requests
import random

# ==========================================
# CONFIGURATION - YOU MUST CHANGE THIS IP
# ==========================================
KALI_VM_IP = "192.168.X.X" # <--- ENTER KALI IP HERE
URL = f"http://{KALI_VM_IP}:80/api/v1/plate-capture"

def simulate_iot_camera():
    print("[*] Booting Edge AI Hardware...")
    print("[*] Initializing Headless IoT Simulator...")
    print(f"[*] Target Server: {URL}")
    print("-" * 40)
    
    mock_plates = ["XYZ-8902", "ABC-1234", "FLK-9981", "STEAL-01", "GHT-5542", "NQR-7711"]
    
    try:
        while True:
            # Simulate the JSON payload from a real ALPR system
            plate_data = {
                "camera_id": "intersection_cam_04",
                "plate_number": random.choice(mock_plates),
                "confidence": round(random.uniform(85.0, 99.9), 2),
                "timestamp": time.time()
            }
            
            print(f"[*] Target Acquired. Transmitting plate [{plate_data['plate_number']}] in plain text...")
            
            try:
                # Send the unencrypted data over the network
                response = requests.post(URL, json=plate_data, timeout=3)
                if response.status_code == 200:
                    print("    -> Transmission successful.")
            except requests.exceptions.RequestException as e:
                print(f"    [!] Transmission failed. Is the Kali server running at {KALI_VM_IP}?")
            
            # Pause randomly between 3 to 7 seconds to simulate natural traffic flow
            time.sleep(random.randint(3, 7))
            
    except KeyboardInterrupt:
        print("\n[*] Powering down IoT Simulator.")

if __name__ == "__main__":
    simulate_iot_camera()