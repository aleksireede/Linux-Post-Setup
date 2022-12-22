#!/bin/bash

function tool_check(){
    if ! command -v $1 &>/dev/null
    then
        /usr/bin/env python3 -m pip install $1
    fi
}

declare -a python_lib=("lolcat" "yt-dlp" "websockets" "GitPython" "pathlib2" "requests" "wakeonlan")
for str in "${python_lib[@]}"; do
    tool_check "$str"
done

/usr/bin/env python3 -m pip install python-telegram-bot -U --pre

export PATH="$PATH:/home/$USER/.local/bin/"
chmod +x ./Installer.py && sudo /usr/bin/env python3 ./Installer.py
cd ..
rm -rf ./Linux-First-Setup
