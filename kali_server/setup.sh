#!/bin/bash
echo "[*] Setting up Kali Server Environment..."
sudo apt-get update
sudo apt-get install -y python3 python3-flask
echo "[+] Setup complete. You can now run server.py"