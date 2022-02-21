#!/bin/bash
grubfile="/etc/default/grub"
customfile="/etc/grub.d/40_custom"
cat <<EOF>> $grubfile
'GRUB_SAVEDEFAULT=true'
EOF
sudo sed -i "s/GRUB_DEFAULT=0/GRUB_DEFAULT=saved/" $grubfile
sudo sed -i "s/GRUB_TIMEOUT=0/GRUB_TIMEOUT=20/" $grubfile
sudo sed -i "s/GRUB_TIMEOUT_STYLE=hidden/GRUB_TIMEOUT_STYLE=menu/" $grubfile

# install windows entry
while true; do
    read -p "Do you want to add windows 11 entry to grub? [Y/n]:" yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

cat <<EOF>> $grubfile
GRUB_DISABLE_OS_PROBER=true
EOF
cat <<EOF>> $customfile
'menuentry 'Windows 11 (kohteella /dev/nvme0n1p1)' --class windows --class os $menuentry_id_option 'windows-efi-7C91-63A3' {'
'    savedefault'
'    insmod part_gpt'
'    insmod fat'
'    if [ x$feature_platform_search_hint = xy ]; then'
'    search --no-floppy --fs-uuid --set=root  7C91-63A3'
'    else'
'    search --no-floppy --fs-uuid --set=root 7C91-63A3'
'    fi'
'    chainloader /EFI/Microsoft/Boot/bootmgfw.efi'
'}'
EOF
