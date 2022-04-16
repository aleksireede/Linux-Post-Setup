#!/bin/bash

## install bash aliases and prompt color etc.
cd ~
wget -O .bash_aliases https://pastebin.com/raw/7B7hmX2a
sed -i -e 's/\r$//' .bash_aliases
source .bash_aliases


if [ -f ~/.bashrc ]
then
#Only for bash
## install bashrc appender
cat << EOF >> ~/.bashrc
if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi
EOF
elif [ -f ~/.zshrc ]
then
#Only for zsh
cat << EOF >> ~/.zshrc
if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi
EOF
else
    echo ""
    echo "Your shell is not supported!"
    echo ""
fi
