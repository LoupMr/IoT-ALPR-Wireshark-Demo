# IoT ALPR Security Testbed

This repository contains a Minimum Viable Product (MVP) testbed designed to evaluate network security boundaries in IoT and AI edge devices. It simulates a misconfigured Automatic License Plate Reader (ALPR) broadcasting unencrypted sensitive data.

This testbed was developed to evaluate the packet analysis capabilities of Wireshark for my Tool Review Project.

## Architecture
* **Backend Server (Kali Linux VM):** Runs a Flask server to receive IoT data. Acts as the monitoring point for Wireshark.
* **IoT Edge Device (Ubuntu VM):** Runs a headless Python script simulating an AI camera extracting license plates and transmitting JSON payloads over HTTP.

## Deployment Instructions

### Step 1: Clone the Repository
Run this command on **both** your Kali Linux and Ubuntu VMs:
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/IoT-ALPR-Wireshark-Demo.git
cd IoT-ALPR-Wireshark-Demo
\`\`\`

### Step 2: Set Up the Kali Server (The Receiver)
1. Navigate to the server directory: `cd kali_server`
2. Make the setup script executable: `chmod +x setup.sh`
3. Run the setup script: `sudo ./setup.sh`
4. Run `ifconfig` or `ip a` on this machine and write down its IP address.
5. Start the server: `sudo python3 server.py`

### Step 3: Set Up the Ubuntu Camera (The Sender)
1. Navigate to the camera directory: `cd ubuntu_camera`
2. Make the setup script executable: `chmod +x setup.sh`
3. Run the setup script: `sudo ./setup.sh`
4. Open `camera.py` in a text editor (like `nano camera.py`).
5. Change the `KALI_VM_IP` variable to the IP address you wrote down in Step 2. Save and exit.
6. Start the camera: `python3 camera.py`

### Step 4: The Wireshark Capture
With both scripts running, open Wireshark on the Kali VM, select your active network interface, and apply the following filter to capture the unencrypted data leak:
\`\`\`text
http.request.method == POST
\`\`\`