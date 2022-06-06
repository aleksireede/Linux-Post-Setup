#!/bin/bash

# Add Universe and Multiverse repos
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:cappelikan/ppa
sudo apt-get update
sudo flatpak install easyeffects

sudo apt --assume-yes -y install \
    fortune cowsay wget eog \
    curl apt-transport-https \
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
    libpipewire-0.3-dev libgtk-4-dev \
    libadwaita-1-dev cmake mainline \
    gnome-software gnupg firefoxpwa

xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search

# Install steam
wget -O steam.deb https://cdn.akamai.steamstatic.com/client/installer/steam.deb
sudo apt install --assume-yes -y ./steam.deb
rm ./steam.deb

# Install fastfetch
git clone https://github.com/LinusDierheimer/fastfetch.git
cd fastfetch/
mkdir -p build
cd build
cmake ..
cmake --build . -j$(nproc) --target fastfetch --target flashfetch
sudo make install
cd ../../
rm -rf ./fastfetch


# Install VSCode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt update
sudo apt install --assume-yes -y code

# Install Syncthing
sudo curl -s -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
sudo apt-get update
sudo apt-get install syncthing

# Update packages
sudo apt --assume-yes -y update
sudo apt --assume-yes -y upgrade
sudo apt --assume-yes -y autoremove
