#!/bin/bash
while true; do
    read -p "Do you want to install discord as native or appimage? [N/a]" yn
    case $yn in
        [Aa]* ) xdg-open https://discord.com/api/download?platform=linux&format=deb; break;;
        [Nn]* ) zap install --github --from=srevinsaju/discord-appImage discord-appimage; break;;
        * ) echo "Please answer yes or no.";;
    esac
done
