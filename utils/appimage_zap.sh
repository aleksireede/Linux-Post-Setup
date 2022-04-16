#!/bin/bash
curl https://raw.githubusercontent.com/srevinsaju/zap/main/install.sh | sudo bash -s
zap install --github --from=srevinsaju/Telegram-AppImage telegram-appimage
zap install --github --from=nextcloud/desktop
