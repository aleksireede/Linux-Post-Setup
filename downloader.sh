#!/usr/bin/env bash
if ! [ command -v pip3 ]  &&  ! [ command -v git ] #check if we have pip and git and if not then install
then
    if [ -f /etc/arch-release ]
    then
        sudo pacman -Sy --needed --noconfirm archlinux-keyring
        sudo pacman -Suy --noconfirm git python3 python-pip
    elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
    then
        sudo apt update
        sudo apt upgrade
        sudo apt install git python3-pip
    elif ! [ command -v termux-setup-storage ]
    then
        apt update
        apt upgrade
        apt install python3 git libxml2 libxslt libiconv
    else
        echo ""
        echo "Your system is not supported!"
        echo ""
        exit
    fi
fi

cd ~
if [ -f ./Linux-First-Setup ]
then
    rm -rf ./Linux-First-Setup
fi

git clone https://github.com/aleksireede/Linux-First-Setup.git
cd ./Linux-First-Setup
chmod +x ./Installer.py
pip3 install -r requirements.txt
./Installer.py
cd ..
rm -rf ./Linux-First-Setup
