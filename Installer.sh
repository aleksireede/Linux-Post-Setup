#!/bin/bash
lolcatbin="/usr/games/lolcat"
function execute(){
    lolcat << EOF
    ┌──────────────────────────────────────────────────────────────────────┐
    │This Bash Script is made by u/Techno021 to nuke snaps from Ubuntu.    │
    │                                                                      │
    │Note: This has only been tested on Ubuntu 20.04 LTS, and may not work │
    │as intended on other versions. I will not be responsible for any      │
    │damage if this script breaks your pc                                  │
    └──────────────────────────────────────────────────────────────────────┘
EOF

    while true; do
        read -p "Do you wish to run the script? [Y/n]:" yn
        case $yn in
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}

function sudocheck(){
    if [[ "$EUID" == 0 ]]
    then 
    lolcat << EOF
    ┌──────────────────────────────────────────────────────────────────────┐
    │Please don't run this script as root as it may break you system.      │
    │We will ask you for the password if we need root access.              │
    └──────────────────────────────────────────────────────────────────────┘
    ┬─┬ ノ( ゜-゜ノ)
EOF
    exit
    fi
}

# Download additional scripts from other sources
cd ./utils/sh
wget https://raw.githubusercontent.com/MasterGeekMX/snap-to-flatpak/main/snap-to-flatpak.sh
cd ../../

if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    # install lolcat
    if [ -f "$lolcatbin" ]; then
        echo "$lolcatbin already exists."
        echo "You don't want to install it twice"
    else
        sudo pacman -S --noconfirm lolcat
    fi
    #end lolcat
    sudocheck
    execute
    chmod u+x ./arch/Packages.sh
    ./arch/Packages.sh
    sudo ./arch/arch.py
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    #install lolcat if not found
    if [ -f "$lolcatbin" ]; then
        echo "$lolcatbin already exists."
        echo "You don't want to install it twice"
    else 
	    cd ~
	    ## install lolcat
	    sudo apt --assume-yes -y install rubygems git
	    git clone https://github.com/aleksireede/lolcat.git
	    cd lolcat/bin
	    sudo gem install lolcat
	    sudo mv lolcat $lolcatbin
	    cd ~
	    rm -rf ./lolcat
    fi
    #end lolcat
    sudocheck
    execute
    chmod u+x ./debian/Packages.sh
    chmod u+x ./debian/doas.sh
    ./debian/Packages.sh
    ./debian/doas.sh
    python ./debian/pulseaudio.py
else
    echo ""
    echo "Your system is not supported!"
    echo ""
    exit
fi
##install all optonal things
chmod u+x ./utils/optional.sh
./utils/optional.sh
curl -sL http://0x0.st/-Y29.cow -o amogus.cow
if [ -f /usr/share/cows/ ]
then
sudo mv ./amogus.cow /usr/share/cows/amogus.cow
fi
if [ -f /usr/share/cowsay/cows/ ]
then
sudo mv ./amogus.cow /usr/share/cowsay/cows/amogus.cow
fi

lolcat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└─────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴ 
EOF
echo
cd ..
rm -rf ./Linux-First-Setup
