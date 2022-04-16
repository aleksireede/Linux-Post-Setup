#!/bin/bash
if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    sudo flatpak install Discord
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    xdg-open https://discord.com/api/download?platform=linux&format=deb
else
    echo ""
    echo "Your system is not supported!"
    echo ""
fi
