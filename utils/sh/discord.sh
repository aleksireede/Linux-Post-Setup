#!/bin/bash
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
while true; do
    read -p "Do you want to install discord as deb or flatpak? [N/f]" yn
    case $yn in
        [Nn]* ) xdg-open https://discord.com/api/download?platform=linux&format=deb; break;;
        [Ff]* ) sudo flatpak install com.discordapp.Discord -y --system; break;;
        * ) echo "Please answer yes or no.";;
    esac
done
