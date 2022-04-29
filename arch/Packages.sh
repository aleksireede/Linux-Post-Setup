#!/bin/bash

# Install apps
paru -Suy --noconfirm --needed \
    brave-bin wit wget curl\
    visual-studio-code-bin \
    premid gst-plugin-pipewire \
    neofetch git supertuxkart \
    base-devel flatpak lsp-plugins\
    p7zip cowsay fortune-mod \
    rubygems pipewire-pulse eog \
    steam discord noto-fonts-cjk\
    gedit vlc gimp libreoffice \
    gparted gnome-disk-utility \
    ufw pamac-aur vim mpv \
    mailspring noto-fonts-emoji-apple \
    pipewire-alsa pipewire-jack  \
    pipewire-v4l2 pipewire-x11-bell \
    easyeffects mda.lv2 opendoas \
    python python-pip python-venv \
    make bison flex keepassxc xdg-utils \
    cifs-utils samba jq rubygems \
    syncthing nextcloud audacious \
    fluidsynth freepats-general-midi \
    soundfont-fluid mpg123 firefox-pwa \
    whatsapp-nativefier dolphin-emu-git \
    archlinux-keyring lunar-client \
    ocs-url appimagelauncher \
    archlinux-appstream-data-pamac \
    downgrade inkscape xorg-xcursorgen \
    googledot-cursor-theme lutris kdenlive \
    wine-ge-custom baobab

#doas    (sudo replacement)[better]{more secure}
wget -O doas.conf https://pastebin.com/raw/EK6hud2S
sudo cp ./doas.conf /etc/doas.conf
sudo chown -c root:root /etc/doas.conf
sudo chmod -c 0400 /etc/doas.conf
paru -S opendoas-sudo
