#!/bin/bash
curl https://raw.githubusercontent.com/srevinsaju/zap/main/install.sh | sudo bash -s
zap install --github --from=srevinsaju/Telegram-AppImage telegram-appimage
zap install --github --from=nextcloud/desktop

curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/srevinsaju/youtube-music-dl
cd youtube-music-dl
poetry install
poetry run cli --help
