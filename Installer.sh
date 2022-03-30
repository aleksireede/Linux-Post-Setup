#!/bin/bash

if [ -f /etc/arch-release ]
then
    #Only for ArchLinux
    chmod u+x ./setup_arch.sh
    ./setup_arch.sh
elif [ -f /etc/lsb-release ] || [ -f /etc/debian_version ] || [ -f /etc/linuxmint/info ]
then
    #Only for Ubuntu/Mint/Debian
    chmod u+x ./setup_debian.sh
    ./setup_debian.sh
else
    echo ""
    echo "Your system is not supported!"
    echo ""
fi
