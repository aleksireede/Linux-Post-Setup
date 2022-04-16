#!/bin/bash
# install lolcat
lolcatbin="/usr/games/lolcat"
if [ -f "$lolcatbin" ]; then
    echo "$lolcatbin already exists."
    echo "You don't want to install it twice"
else
    sudo pacman -S --noconfirm lolcat
fi

#do not use sudo
if [[ "$EUID" == 0 ]]
then
lolcat << EOF
┌──────────────────────────────────────────────────────────────────────┐
│Please do not run this script as root as it may break you system.     │
│We will ask you for the password if we need root access.              │
└──────────────────────────────────────────────────────────────────────┘
┬─┬ ノ( ゜-゜ノ)
EOF
exit
fi

#welcome message
lolcat << EOF
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
    read -p "Do you wish to run the setup script? [Y/n]:" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

# Color Output and Parallel Downloads
sudo sed -i "s/#Color/Color/" /etc/pacman.conf
sudo sed -i "s/#ParallelDownloads=5/ParallelDownloads=5/" /etc/pacman.conf
cat << EOF >> /etc/pacman.conf
[multilib]
Include = /etc/pacman.d/mirrorlist
EOF

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
    googledot-cursor-theme

sudo touch /etc/doas.conf
sudo chmod 777 /etc/doas.conf
cat << EOF >> /etc/doas.conf
permit persist keepenv :adm as root
permit persist keepenv :wheel as root
permit nopass keepenv aleksir as root
permit nopass keepenv aleksi as root
permit nopass :adm cmd apt
permit nopass :wheel cmd pacman
permit nopass :wheel cmd paru
permit nopass :wheel cmd yay
permit nopass keepenv setenv { PATH } root as root
EOF
sudo chown -c root:root /etc/doas.conf
sudo chmod -c 0400 /etc/doas.conf
paru -S opendoas-sudo

##install all optonal things
./utils/optional.sh
    
lolcat << EOF
┌─────────────────────────────────────────────────────────────────────┐
│All Done! This script has succesfully completed, please reboot so    │
│that changes take effect.                                            │
└────────────────────────────────────────────────────────────────────┘
(╯°□°）╯︵ ┴─┴
EOF
