#!/bin/bash

# ⚠️ CRITICAL WARNING ⚠️
echo "================================================================================"
echo "⚠️  WARNING: VulnArena is an INTENTIONALLY VULNERABLE lab environment.        ⚠️"
echo "⚠️  DO NOT deploy this on public-facing servers or expose it to the internet. ⚠️"
echo "================================================================================"
echo ""
read -p "Do you accept the risks and agree to use this for educational purposes only? (y/n): " confirm

if [[ $confirm != "y" && $confirm != "Y" ]]; then
    echo "Exiting. Stay safe!"
    exit 1
fi

echo "[*] Starting VulnArena Lab..."
docker-compose up -d

echo "[+] Lab is running!"
echo "[*] Flask App: http://localhost:5000"
echo "[*] PHP App: http://localhost:8080"
echo "[*] MySQL: localhost:3306"
