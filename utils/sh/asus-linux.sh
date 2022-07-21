#!/bin/bash
if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    git clone https://gitlab.com/asus-linux/asusctl.git
    cd asusctl
    make
    sudo make install
    cd ..
    sudo rm -rf ./asusctl
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    sudo apt install libclang-dev libudev-dev
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    source $HOME/.cargo/env
    git clone https://gitlab.com/asus-linux/asusctl.git
    cd asusctl
    make
    sudo make install
    cd ..
    sudo rm -rf ./asusctl
else
    echo ""
    echo "Your system is not supported!"
    echo ""
fi
