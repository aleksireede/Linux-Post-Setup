#!/bin/bash
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

function optional(){
	##install all optonal things
	chmod +x ./utils/optional.sh
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
}

# Download additional scripts from other sources
cd ./utils/sh
wget https://raw.githubusercontent.com/MasterGeekMX/snap-to-flatpak/main/snap-to-flatpak.sh
cd ../../

if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    if ! command -v lolcat &> /dev/null
    then
        sudo pacman -S --noconfirm lolcat
    fi
    sudocheck
    execute
    chmod +x ./arch/Packages.sh
    ./arch/Packages.sh
    optional
    chmod +x ./arch/arch.py
    sudo ./arch/arch.py
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    if ! command -v lolcat &> /dev/null
    then
        chmod +x ./utils/lolcat.sh
        ./utils/lolcat.sh
    fi
    sudocheck
    execute
    chmod +x ./debian/Packages.sh
    chmod +x ./debian/doas.sh
    ./debian/Packages.sh
    ./debian/doas.sh
    optional
    ./debian/pulseaudio.py
else
    echo ""
    echo "Your system is not supported!"
    echo ""
    exit
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
