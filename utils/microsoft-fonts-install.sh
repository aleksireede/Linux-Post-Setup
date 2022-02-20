#!/bin/bash
if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    yay -Suy ttf-ms-fonts
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    sudo apt update && sudo apt install --assume-yes -y ttf-mscorefonts-installer
else
    echo ""
    echo "Your system is not supported!"
    echo ""
fi
