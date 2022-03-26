#!/bin/bash
# Install Discord as appimage
curl https://raw.githubusercontent.com/srevinsaju/zap/main/install.sh | sudo bash -s
zap install --github --from=srevinsaju/discord-appImage discord-appimage
zap install --github --from=srevinsaju/Telegram-AppImage telegram-appimage
curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/srevinsaju/youtube-music-dl
cd youtube-music-dl
poetry install
poetry run cli --help

if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    chmod u+x ./setup_arch.sh
    ./setup_arch.sh
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    chmod u+x ./setup_debian.sh
    ./setup_debian.sh
else
    echo ""
    echo "Your system is not supported!"
    echo ""
fi
