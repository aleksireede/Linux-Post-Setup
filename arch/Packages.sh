#!/bin/bash

# Install Yay
git clone https://aur.archlinux.org/paru.git/
cd paru
makepkg -si
cd ..
rm -rf paru/

sudo rm -rf /etc/pacman.conf
sudo chmod 777 /etc/pacman.conf
curl https://pastebin.com/raw/hJi4icEy >/etc/pacman.conf
sudo chmod 644 /etc/pacman.conf
sudo pacman-key --recv-keys F3B607488DB35A47 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key F3B607488DB35A47
sudo pacman -U 'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-keyring-2-1-any.pkg.tar.zst' 'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-mirrorlist-8-1-any.pkg.tar.zst' 'https://mirror.cachyos.org/repo/x86_64/cachyos/cachyos-v3-mirrorlist-8-1-any.pkg.tar.zst'
/lib/ld-linux-x86-64.so.2 --help | grep "x86-64-v3 (supported, searched)"

# Install apps
paru -Suy --noconfirm --needed \
    brave-bin wit wget curl\
    visual-studio-code-bin \
    premid gst-plugin-pipewire \
    neofetch-btw git supertuxkart \
    base-devel-meta flatpak lsp-plugins\
    p7zip cowsay fortune-mod \
    rubygems pipewire-pulse eog \
    steam discord noto-fonts-cjk\
    gedit vlc gimp libreoffice \
    gparted gnome-disk-utility \
    ufw pamac-aur vim mpv \
    noto-fonts-emoji-apple \
    pipewire-alsa pipewire-jack  \
    pipewire-v4l2 pipewire-x11-bell \
    easyeffects mda.lv2 opendoas \
    python python-pip \
    make bison flex keepassxc xdg-utils \
    cifs-utils samba jq rubygems \
    syncthing nextcloud audacious \
    fluidsynth freepats-general-midi \
    soundfont-fluid mpg123 firefox-pwa-bin \
    whatsapp-nativefier dolphin-emu-git \
    archlinux-keyring lunar-client \
    ocs-url appimagelauncher \
    archlinux-appstream-data-pamac \
    downgrade inkscape xorg-xcursorgen \
    googledot-cursor-theme lutris kdenlive \
    baobab syncthing-gtk-python3 \
    btw wine-gecko wine-mono winetricks \
    wine

#doas    (sudo replacement)[better]{more secure}
wget -O doas.conf https://pastebin.com/raw/EK6hud2S
sudo cp ./doas.conf /etc/doas.conf
sudo chown -c root:root /etc/doas.conf
sudo chmod -c 0400 /etc/doas.conf
paru -S opendoas-sudo
