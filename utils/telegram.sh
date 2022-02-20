#!/bin/bash
# Install telegram
InstallPath="/usr/share/aleksireede/Telegram"
wget -O telegram.tar.xz https://telegram.org/dl/desktop/linux
tar -xf telegram.tar.xz
rm telegram.tar.xz
cd Telegram
mkdir $InstallPath
sudo mv Telegram $InstallPath
sudo mv Updater $InstallPath
$InstallPath/Updater
