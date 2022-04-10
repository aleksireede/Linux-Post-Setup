#!/bin/bash
while true; do
    read -p "Do you want to install discord as native or flatpak? [N/f]" yn
    case $yn in
        [Ff]* ) xdg-open https://discord.com/api/download?platform=linux&format=deb; break;;
        [Nn]* ) sudo flatpak install Discord; break;;
        * ) echo "Please answer yes or no.";;
    esac
done
