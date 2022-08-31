#!/bin/bash

# Add Universe and Multiverse repos
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:cappelikan/ppa
sudo add-apt-repository ppa:flexiondotorg/mangohud
sudo dpkg --add-architecture i386 

sudo apt -qq --assume-yes -y install \
curl apt-transport-https \
gnupg

wget -qO- https://Wiener234.github.io/ani-cli-ppa/KEY.gpg | sudo tee /etc/apt/trusted.gpg.d/ani-cli.asc
wget -qO- https://Wiener234.github.io/ani-cli-ppa/ani-cli-debian.list | sudo tee /etc/apt/sources.list.d/ani-cli-debian.list

curl -fsSL https://packagecloud.io/filips/FirefoxPWA/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/firefoxpwa-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/firefoxpwa-keyring.gpg] https://packagecloud.io/filips/FirefoxPWA/any any main" | sudo tee /etc/apt/sources.list.d/firefoxpwa.list > /dev/null

curl https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg | sudo tee /usr/share/keyrings/grapejuice-archive-keyring.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/grapejuice.list <<< 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main' > /dev/null
bash <(wget -qO- https://raw.githubusercontent.com/Heroic-Games-Launcher/HeroicGamesLauncher/main/rauldipeas.sh)

sudo apt-get -qq update
flatpak install flathub com.github.wwmm.easyeffects
flatpak install flathub com.lunarclient.LunarClient

sudo apt -qq --assume-yes -y install \
    fortune-mod cowsay wget eog \
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
    gnome-software gnupg firefoxpwa \
    dos2unix kate keepassxc inkscape \
    libpam0g-dev cmake aptitude synaptic \
    goverlay meson libdbus-1-dev glslang-dev \
    glslang-tools libxnvctrl-dev wine64 \
    wine32 libasound2-plugins:i386 \
    libsdl2-2.0-0:i386 libdbus-1-3:i386 \
    libsqlite3-0:i386 mono-complete \
    grapejuice eog-plugins \
    gnome-software-plugin-flatpak \
    gnome-tweaks nemo-gtkhash ani-cli

xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search

# Install steam
wget -O steam.deb https://cdn.akamai.steamstatic.com/client/installer/steam.deb
sudo apt -qq install --assume-yes -y ./steam.deb
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
sudo apt -qq update
sudo apt -qq --assume-yes -y install code

# Install Syncthing
sudo curl -s -o /usr/share/keyrings/syncthing-archive-keyring.gpg https://syncthing.net/release-key.gpg
echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable" | sudo tee /etc/apt/sources.list.d/syncthing.list
sudo apt-get -qq update
sudo apt-get -qq -y --assume-yes install syncthing

# Update packages
sudo apt -qq --assume-yes -y update
sudo apt -qq --assume-yes -y upgrade
sudo apt -qq --assume-yes -y autoremove
