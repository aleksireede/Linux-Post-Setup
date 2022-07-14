#!/usr/bin/env bash
lolcatbin="/usr/games/lolcat"
cd ~
## install lolcat
sudo apt --assume-yes -y install rubygems git
git clone https://github.com/aleksireede/lolcat.git
cd lolcat/bin
sudo gem install lolcat
sudo mv lolcat $lolcatbin
cd ~
rm -rf ./lolcat
