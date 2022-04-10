#!/bin/bash
function telegram-native(){
    InstallPath="/usr/share/aleksireede/Telegram"
    wget -O telegram.tar.xz https://telegram.org/dl/desktop/linux
    tar -xf telegram.tar.xz
    rm telegram.tar.xz
    cd Telegram
    mkdir $InstallPath
    sudo mv Telegram $InstallPath
    sudo mv Updater $InstallPath
    $InstallPath/Updater
    }
while true; do
    read -p "Do you want to install telegram as native or flatpak? [N/f]" yn
    case $yn in
        [Nn]* ) telegram-native; break;;
        [Ff]* ) sudo flatpak install org.telegram -y --system; break;;
        * ) echo "Please answer yes or no.";;
    esac
done
