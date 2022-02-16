#!/bin/bash

## install bash aliases and prompt color etc.
cd ~
wget -O .bash_aliases https://pastebin.com/raw/7B7hmX2a
sed -i -e 's/\r$//' .bash_aliases
source .bash_aliases

## install bashrc appender
cd ~
cat << EOF >> .bashrc
if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi
EOF
