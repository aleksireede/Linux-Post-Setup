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

# Add Universe and Multiverse repos
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo apt-get update

sudo apt --assume-yes -y install \
	neofetch fortune cowsay wget \
    curl apt-transport-https rubygems \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    python3 python3-pip python3-venv git \
    p7zip-full p7zip-rar software-properties-common \
    lsp-plugins

#install lolcat if not found
FILE="/usr/games/lolcat"
if [ -f "$FILE" ]; then
    echo "$FILE already exists."
    echo "You don't want to install it twice"
else 
	cd ~
	## install lolcat
	sudo apt install rubygems cowsay neofetch fortune
	wget https://github.com/aleksireede/lolcat/archive/master.zip
	unzip master.zip
	rm master.zip
	cd lolcat-master/bin
	sudo gem install lolcat
	sudo mv lolcat /usr/games/lolcat
fi

# Install VSCode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg

sudo apt-get update
sudo apt-get install --assume-yes code

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# Install Flatpak
sudo apt install flatpak
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

##install optional stuff
./utils/optional.sh


cat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└─────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴ 
EOF
echo
