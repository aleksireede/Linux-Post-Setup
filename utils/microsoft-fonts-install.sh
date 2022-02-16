#!/bin/bash
read -p "Path to windows iso: " file
if [[ -f $file ]]
then
    7z e $file sources/install.wim
    sudo 7z e install.wim 1/Windows/{Fonts/"*".{ttf,ttc},System32/Licenses/neut>
    rm install.wim
    sudo chmod 655 /usr/share/fonts/WindowsFonts/
    fc-cache --force
else
    echo "Windows iso not found, skipping microsoft fonts installation."
fi
