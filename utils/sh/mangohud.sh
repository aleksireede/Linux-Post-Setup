#!/usr/bin/env bash
git clone --recurse-submodules https://github.com/flightlessmango/MangoHud.git
cd MangoHud
chmod +x ./build.sh
./build.sh build
cd ..
sudo rm -rf ./Mangohud
