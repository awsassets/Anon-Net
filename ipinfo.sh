#!/bin/bash
echo "[+] Waiting for IP information"

while :;do let i++;var=$(curl -s ifconfig.me)&>/dev/null &&echo -e "[+]Current IP:\033[32m$var\033[0m" && sleep 30;done;

export http_proxy=127.0.0.1:8123
export https_proxy=127.0.0.1:8123