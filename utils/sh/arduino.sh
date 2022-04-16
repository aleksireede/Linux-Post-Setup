#!/bin/bash
sudo mkdir /usr/share/aleksireede && cd /usr/share/aleksireede
sudo wget https://downloads.arduino.cc/arduino-nightly-linux64.tar.xz
sudo tar -xf arduino-nightly-linux64.tar.xz
sudo rm arduino-nightly-linux64.tar.xz && cd ./arduino-nightly
./arduino-linux-setup.sh $USER
sudo ./install.sh
