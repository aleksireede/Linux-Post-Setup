#!/bin/bash
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
while true; do
    read -p "Do you want to install discord as debian or arch or flatpak? [D/f/a]" yn
    case $yn in
        [Dd]* ) xdg-open https://discord.com/api/download?platform=linux&format=deb; break;;
        [Ff]* ) sudo flatpak install com.discordapp.Discord -y --system; break;;
        [Aa]* ) sudo pacman -S discord; break;;
        * ) echo "Please answer.";;
    esac
done
