#!/bin/bash
#install lolcat if not found
lolFILE="/usr/games/lolcat"
if [ -f "$lolFILE" ]; then
    echo "$lolFILE already exists."
    echo "You don't want to install it twice"
else 
	cd ~
	## install lolcat
    sudo apt --assume-yes -y install rubygems
	wget https://github.com/aleksireede/lolcat/archive/master.zip
	unzip master.zip
	rm master.zip
	cd lolcat-master/bin
	sudo gem install lolcat
	sudo mv lolcat /usr/games/lolcat
fi

if [[ "$EUID" == 0 ]]
then
if [ -f "$lolFILE" ]; then
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

if [ -f "$lolFILE" ]; then
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

sudo apt --assume-yes -y install \
    neofetch fortune cowsay wget eog \
    curl apt-transport-https pulseaudio \
    openjdk-8-jre openjdk-11-jre openjdk-17-jre \
    python3 python3-pip python3-venv git \
    p7zip-full p7zip-rar software-properties-common \
    lsp-plugins gedit gnome-disk-utlity gparted \
    supertuxkart pulseeffects pulseaudio-equalizer \
    libpulse-java
    
while true; do
    read -p "Do you want to install discord? [Y/n]" yn
    case $yn in
        [Yy]* ) xdg-open https://discord.com/api/download?platform=linux&format=deb; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

# Install VSCode 
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg
sudo apt update
sudo apt install --assume-yes -y code

# Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt --assume-yes -y install ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# Install Flatpak
sudo apt --assume-yes -y install flatpak
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Install brave-browser
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt --assume-yes -y install brave-browser

# Install enpass
sudo -i
echo "deb https://apt.enpass.io/ stable main" > \
  /etc/apt/sources.list.d/enpass.list
wget -O - https://apt.enpass.io/keys/enpass-linux.key | tee /etc/apt/trusted.gpg.d/enpass.asc
apt-get update
apt-get install enpass
exit

# Install premid 
curl -s https://packagecloud.io/install/repositories/PreMiD/Linux/script.deb.sh | sudo os=Ubuntu dist=hirsute bash
sudo apt install --assume-yes -y premid

##install optional stuff
chmod u+x ./utils/optional.sh
./utils/optional.sh
sudo apt update
sudo apt --assume-yes -y upgrade


cat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└─────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴ 
EOF
echo
