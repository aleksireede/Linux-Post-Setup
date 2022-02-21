#!/bin/bash
chmod u+x ./utils/microsoft-fonts-install.sh
chmod u+x ./utils/snap-nuke.sh
chmod u+x ./utils/bash_aliases.sh
chmod u+x ./utils/wiim_install.sh
chmod u+x ./utils/noto-color-emoji.sh
chmod u+x ./utils/arduino.sh
chmod u+x ./utils/telegram.sh
chmod u+x ./utils/grub.sh

# Microsoft Fonts Install
while true; do
    read -p "Do you wish to install microsoft fonts? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/microsoft-fonts-install.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

# Snap Remove
while true; do
    read -p "Do you wish to remove the snap package manager? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/snap-nuke.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

## Install bash aliases
while true; do
    read -p "Do you want to install bash aliases? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/bash_aliases.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

#install wiims iso and szs tools
while true; do
    read -p "Do you want to install wiimms iso and szs tools? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/wiim_install.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

#install latest noto-color-emoji.ttf
while true; do
    read -p "Do you want to install Noto color emoji font? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/noto-color-emoji.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done

#install telegram
while true; do
    read -p "Do you want to install Telegram? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/telegram.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done

#install arduino
while true; do
    read -p "Do you want to install Arduino? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/arduino.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done

#install grub fixes
while true; do
    read -p "Do you want to make changes to grub? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/grub.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done
