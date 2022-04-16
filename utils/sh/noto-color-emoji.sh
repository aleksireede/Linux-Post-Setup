#!/bin/bash
wget https://github.com/googlefonts/noto-emoji/raw/main/fonts/NotoColorEmoji.ttf
if [ -f /usr/share/fonts/truetype/ ]
then
sudo mv NotoColorEmoji.ttf /usr/share/fonts/truetype/
fi
if [ -f /usr/share/fonts/noto/ ]
then
sudo mv NotoColorEmoji.ttf /usr/share/fonts/noto/
fi
