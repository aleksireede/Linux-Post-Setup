#Install doas
git clone https://github.com/slicer69/doas.git
cd ./doas
make
sudo make install
wget -O doas.conf https://pastebin.com/raw/EK6hud2S
sudo chmod 0400 ./doas.conf
sudo chown root:root ./doas.conf
sudo dos2unix ./doas.conf
sudo cp ./doas.conf /usr/local/etc/doas.conf
cd ..
rm -rf ./doas
