#!/bin/sh
if [ -f /etc/arch-release ]
then
    sudo pacman -S --noconfirm git python3 python-pip
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    sudo apt install git python3-pip
else
    echo ""
    echo "Your system is not supported!"
    echo ""
    exit
fi
cd ~
git clone https://github.com/aleksireede/Linux-First-Setup.git
cd ./Linux-First-Setup
chmod +x ./Installer.py
pip install -r requirements.txt
./Installer.py
cd ..
rm -rf ./Linux-First-Setup