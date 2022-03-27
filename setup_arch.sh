#!/bin/bash
# install lolcat
lolcatbin="/usr/games/lolcat"
if [ -f "$lolcatbin" ]; then
    echo "$lolcatbin already exists."
    echo "You don't want to install it twice"
else 
	sudo pacman -S --noconfirm lolcat
fi

#do not use sudo
if [[ "$EUID" == 0 ]]
then
if [ -f "$lolcatbin" ]; then
    lolcat << EOF
else
    cat << EOF
┌──────────────────────────────────────────────────────────────────────┐
│Please do not run this script as root as it may break you system.     │
│We will ask you for the password if we need root access.              │
└──────────────────────────────────────────────────────────────────────┘
┬─┬ ノ( ゜-゜ノ)
EOF
exit
fi

#welcome message
if [ -f "$lolcatbin" ]; then
    lolcat << EOF
else
    cat << EOF
┌──────────────────────────────────────────────────────────────────────┐
|-This Script can install the following stuff on your linux pc:        |
|*Flatpak                                                              |
|*Vscode                                                               |
|*Google Chrome                                                        |
|*Git                                                                  |
|*Python3                                                              |
|*Brave browser                                                        |
|*Neofetch                                                             |
|*Lsp-plugins                                                          |
|*Cowsay                                                               |
|*Lolcat                                                               |
|*Openjdk-jre v8 v11 v17                                               |
|*Discord                                                              |
|*Supertuxkart                                                         |
|*Gedit                                                                |
|*Gparted                                                              |
|*Steam                                                                |
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

# Color Output and Parallel Downloads
sudo sed -i "s/#Color/Color/" /etc/pacman.conf
sudo sed -i "s/#ParallelDownloads=5/ParallelDownloads=5/" /etc/pacman.conf

cat << EOF >> /etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist
EOF

# Update System
sudo pacman -Syu

# Install Things 
sudo pacman -S --noconfirm \
    neofetch git \
    base-devel curl wget \
    p7zip cowsay fortune \
    rubygems lsp-plugins \
    python python-pip \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    flatpak steam discord eog \
    gedit vlc gimp libreoffice \
    gparted gnome-disk-utility

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
    premid enpass-bin \
    pulseeffects-legacy \
    supertuxkart-git

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
