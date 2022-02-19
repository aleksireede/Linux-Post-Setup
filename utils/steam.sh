#!/bin/bash
wget -O steam.deb https://cdn.akamai.steamstatic.com/client/installer/steam.deb
sudo apt install --assume-yes -y ./steam.deb
