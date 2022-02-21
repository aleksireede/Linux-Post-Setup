#!/bin/bash
$grubfile="/etc/default/grub"
cat << EOF >> $grubfile
GRUB_SAVEDEFAULT=true
EOF
sudo sed -i "s/GRUB_DEFAULT=0/GRUB_DEFAULT=saved/" $grubfile
sudo sed -i "s/GRUB_TIMEOUT=0/GRUB_TIMEOUT=20/" $grubfile
sudo sed -i "s/GRUB_TIMEOUT_STYLE=hidden/GRUB_TIMEOUT_STYLE=menu/" $grubfile
