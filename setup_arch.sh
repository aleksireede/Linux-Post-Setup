#!/bin/bash

if [[ "$EUID" == 0 ]]
then 
cat << EOF
┌──────────────────────────────────────────────────────────────────────┐
│Please don't run this script as root as it may break you system.      │
│We will ask you for the password if we need root access.              │
└──────────────────────────────────────────────────────────────────────┘
┬─┬ ノ( ゜-゜ノ)
EOF
exit
fi

cat << EOF
┌──────────────────────────────────────────────────────────────────────┐
|-This Script can install the following stuff on your linux pc:        |
|*Flatpak                                                              |
|*microsft fonts                                                       |
|*vscode                                                               |
|*chrome                                                               |
|*git                                                                  |
|*python3                                                              |
|*brave browser                                                        |
|*neofetch                                                             |
|*lsp-plugins                                                          |
|*cowsay                                                               |
|*lolcat                                                               |
|*openjdk-jre v8 v11 v17                                               |
│                                                                      │
│Optionally:install Wiimms iso and szs tools,                          │
│install Microfost Fonts(iso required), install bash aliases file      |
|and remove the snap package manager.                                  │
└──────────────────────────────────────────────────────────────────────┘
EOF

while true; do
    read -p "Do you wish to run the setup script? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
# Update System
sudo pacman -Syu

# Color Output and Parallel Downloads
sudo sed -i "s/#Color/Color/" /etc/pacman.conf
sudo sed -i "s/#ParallelDownloads=5/ParallelDownloads=5/" /etc/pacman.conf

# Install Things 
sudo pacman -S --noconfirm \
    neofetch lolcat git \
    base-devel curl wget \
    p7zip cowsay fortune \
    rubygems lsp-plugins \
    python python-pip \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    flatpak

# Install Yay
git clone https://aur.archlinux.org/yay.git/
cd yay
makepkg -si
cd ..
rm -rf yay/

# Install More things
yay -S \
    brave-bin google-chrome \
    visual-studio-code-bin \

##install all optonal things
./utils/optional.sh
    
cat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└─────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴ 
EOF
echo
