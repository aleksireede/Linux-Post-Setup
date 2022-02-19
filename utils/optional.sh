#!/bin/bash
chmod u+x ./utils/microsoft-fonts-install.sh
chmod u+x ./utils/snap-nuke.sh
chmod u+x ./utils/bash_aliases.sh
chmod u+x ./utils/wiim_install.sh
chmod u+x ./utils/noto-color-emoji.sh
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

## Install custom run_once script
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

#install steam
while true; do
    read -p "Do you want to install Steam? [Y/n]:" yn
    case $yn in
        [Yy]* ) ./utils/steam.sh; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no";;
    esac
done
