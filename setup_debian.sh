#!/bin/bash

#install lolcat if not found
lolFILE="/usr/games/lolcat"
if [ -f "$lolFILE" ]; then
    echo "$lolFILE already exists."
    echo "You don't want to install it twice"
else 
	cd ~
	## install lolcat
	sudo apt --assume-yes -y install rubygems git
	git clone https://github.com/aleksireede/lolcat.git
	cd lolcat/bin
	sudo gem install lolcat
	sudo mv lolcat /usr/games/lolcat
	cd ~
	rm -rf ./lolcat
fi

if [[ "$EUID" == 0 ]]
then
lolcat << EOF
┌──────────────────────────────────────────────────────────────────────┐
│Please do not run this script as root as it may break you system.     │
│We will ask you for the password if we need root access.              │
└──────────────────────────────────────────────────────────────────────┘
┬─┬ ノ( ゜-゜ノ)
EOF
exit
fi

lolcat << EOF
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
    read -p "Do you wish to run the setup script? [Y/n]" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

# Add Universe and Multiverse repos
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository ppa:stk/dev
sudo apt-get update
curl -s https://packagecloud.io/install/repositories/PreMiD/Linux/script.deb.sh | sudo os=Ubuntu dist=impish bash

sudo apt --assume-yes -y install \
    neofetch fortune cowsay wget eog \
    curl apt-transport-https pulseaudio \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    python3 python3-pip python3-venv git \
    p7zip-full p7zip-rar software-properties-common \
    lsp-plugins gedit gnome-disk-utility gparted \
    supertuxkart pulseeffects pulseaudio-equalizer \
    libpulse-java vlc libreoffice gimp \
    build-essential make bison flex libpam0g-dev \
    keepassxc xdg-utils jq flatpak \
    vim mpv

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

#Install doas
git clone https://github.com/slicer69/doas.git
cd ./doas
make
sudo make install
sudo chmod 777 /usr/local/etc/doas.conf
cat << EOF >> /usr/local/etc/doas.conf
permit persist keepenv :adm as root
permit nopass keepenv aleksir as root
permit nopass keepenv aleksi as root
permit nopass :adm cmd apt
permit nopass keepenv setenv { PATH } root as root
EOF
sudo chmod 644 /usr/local/etc/doas.conf
cd ..
rm -rf ./doas

##install optional stuff
chmod u+x ./utils/optional.sh
./utils/optional.sh

# Update packages
sudo apt --assume-yes -y update
sudo apt --assume-yes -y upgrade
sudo apt --assume-yes -y autoremove

python ./utils/pulseaudio.py

lolcat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└─────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴ 
EOF
