#!/bin/bash
git clone https://github.com/varlesh/oreo-cursors.git
cd oreo-cursors
ruby generator/convert.rb
make build
sudo make install
cd ..
sudo rm ./oreo-cursors
