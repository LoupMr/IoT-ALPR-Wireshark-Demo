#!/bin/bash
echo "[*] Setting up Ubuntu IoT Camera Environment..."
sudo apt-get update
sudo apt-get install -y python3 python3-requests
echo "[+] Setup complete. Please update the IP address in camera.py before running."