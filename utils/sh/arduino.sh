#!/bin/bash
readarray -d '' cwd < <(pwd)
if [ ! -f /usr/share/aleksireede ]
then
    sudo mkdir /usr/share/aleksireede
fi
cd /usr/share/aleksireede
if [ -f ./arduino-nightly ]
then
    sudo rm -rf ./arduino-nightly
fi
sudo wget https://downloads.arduino.cc/arduino-nightly-linux64.tar.xz
sudo tar -xf arduino-nightly-linux64.tar.xz
sudo rm arduino-nightly-linux64.tar.xz 
cd ./arduino-nightly
./arduino-linux-setup.sh $USER
sudo ./install.sh
cd $cwd
