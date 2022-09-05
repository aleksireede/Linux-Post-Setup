#!/bin/bash

# Install apps
pacman -S base-devel

# Install paru
if ! command -v paru &> /dev/null
    then
    git clone https://aur.archlinux.org/paru.git/
    cd paru
    makepkg -si
    cd ..
    rm -rf paru/
fi

paru -Suy --needed --quiet \
    wit wget curl\
    visual-studio-code-bin \
    premid gst-plugin-pipewire \
    fastfetch git \
    base-devel-meta flatpak lsp-plugins\
    p7zip cowsay fortune-mod \
    rubygems pipewire-pulse eog \
    discord noto-fonts-cjk\
    gedit vlc gimp libreoffice \
    gparted gnome-disk-utility \
    ufw vim mpv \
    noto-fonts-emoji-apple \
    pipewire-alsa pipewire-jack  \
    pipewire-v4l2 pipewire-x11-bell \
    easyeffects mda.lv2 opendoas \
    python python-pip \
    make bison flex keepassxc xdg-utils \
    cifs-utils samba jq rubygems \
    syncthing-gtk-python3 nextcloud audacious \
    fluidsynth freepats-general-midi \
    soundfont-fluid mpg123 firefox-pwa-bin \
    whatsapp-nativefier \
    archlinux-keyring \
    ocs-url appimagelauncher \
    downgrade inkscape xorg-xcursorgen \
    googledot-cursor-theme lutris kdenlive \
    baobab syncthing-gtk-python3 \
    btw android-tools firefox dos2unix \
    xdg-utils steam nextcloud-client \
    firefox-pwa-bin nemo nemo-fileroller \
    nemo-compare nemo-preview nemo-seahorse \
    nemo-share nemo-terminal nemo-megasync \
    nemo-media-columns nemo-pdf-tools \
    nemo-folder-icons nemo-image-converter-git\
    nemo-dropbox nemo-pastebin-git\
    nemo-run-with-nvidia nemo-python-git\
    nemo-audio-tab-git lutris \
    proton-ge-custom-bin \
    protonup-qt goverlay-bin \
    gnome-console woeusb-ng \
    syncthingtray-qt6 boost-libs-git \
    c++utilities qtforkawesome-qt6 \
    qtutilities-qt6 gnome-todo \
    mcpelauncher-linux-git rclone-bin \
    mcpelauncher-ui-git kdeconnect \
    gvfs-smb appimagelauncher \
    eovpn telegram-desktop-bin \
    cemu-experimental-wine \
    grapejuice
flatpak install easyeffects

#doas    (sudo replacement)[better]{more secure}
if ! [ -f /etc/doas.conf ]
then
    xdg-open https://pastebin.com/raw/EK6hud2S
    sudo vim /etc/doas.conf
    paru -S opendoas-sudo
fi
