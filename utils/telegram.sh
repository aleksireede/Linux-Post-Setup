#!/bin/bash
# Install telegram
wget -O telegram.tar.xz https://telegram.org/dl/desktop/linux
tar -xf telegram.tar.xz
rm telegram.tar.xz
cd Telegram
sudo mv Telegram /usr/share/
sudo mv Updater /usr/share/
/usr/share/Updater
