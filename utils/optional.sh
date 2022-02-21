#!/bin/bash
chmod u+x ./utils/microsoft-fonts-install.sh
chmod u+x ./utils/snap-nuke.sh
chmod u+x ./utils/bash_aliases.sh
chmod u+x ./utils/wiim_install.sh
chmod u+x ./utils/noto-color-emoji.sh
chmod u+x ./utils/arduino.sh
chmod u+x ./utils/telegram.sh
chmod u+x ./utils/grub.sh

function utility(){
    while true; do
        read -p "$1 [Y/n]:" yn
        case $yn in
            [Yy]* ) $2; break;;
            [Nn]* ) break;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

utility "Do you want to install microsoft fonts?" ./utils/microsoft-fonts-install.sh # Microsoft Fonts Install
utility "Do you wish to remove the snap package manager?" ./utils/snap-nuke.sh # Snap Remove
utility "Do you want to install bash aliases?" ./utils/bash_aliases.sh # Install bash aliases
utility "Do you want to install wiimms iso and szs tools?" ./utils/wiim_install.sh #install wiims iso and szs tools
utility "Do you want to install Noto color emoji font?" ./utils/noto-color-emoji.sh #install latest noto-color-emoji.ttf
utility "Do you want to install Telegram?" ./utils/telegram.sh #install telegram
utility "Do you want to install Arduino?" ./utils/arduino.sh #install arduino
utility "Do you want to make changes to grub?" ./utils/grub.sh #install grub fixes
