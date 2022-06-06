#!/bin/bash

# Add Universe and Multiverse repos
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:stk/dev
sudo add-apt-repository ppa:embrosyn/cinnamon
sudo apt-get update
curl -s https://packagecloud.io/install/repositories/PreMiD/Linux/script.deb.sh | sudo os=Ubuntu dist=impish bash

sudo flatpak install easyeffects

sudo apt --assume-yes -y install \
    neofetch fortune cowsay wget eog \
    curl apt-transport-https pulseaudio \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    python3 python3-pip python3-venv git \
    p7zip-full p7zip-rar software-properties-common \
    lsp-plugins gedit gnome-disk-utility gparted \
    supertuxkart libzita-convolver-dev \
    libpulse-java libreoffice gimp \
    build-essential make bison flex libpam0g-dev \
    keepassxc xdg-utils jq flatpak \
    vim mpv audacious htop inkscape \
    kate kdenlive nemo-nextcloud nemo \
    synaptic gdebi itstool libtbb2-dev \
    libpipewire-0.3-dev libgtk-4-dev

# Install steam
wget -O steam.deb https://cdn.akamai.steamstatic.com/client/installer/steam.deb
sudo apt install --assume-yes -y ./steam.deb
rm ./steam.deb

# Install VSCode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt update
sudo apt install --assume-yes -y code

# Install brave-browser
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt --assume-yes -y install brave-browser

# Install Syncthing
sudo curl -s -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
sudo apt-get update
sudo apt-get install syncthing

# Update packages
sudo apt --assume-yes -y update
sudo apt --assume-yes -y upgrade
sudo apt --assume-yes -y autoremove
