#!/bin/bash
if ! command -v lolcat &> /dev/null
then
    /usr/bin/env python3 -m pip install lolcat pathlib2 yt-dlp websockets GitPython
fi
chmod +x ./Installer.py
./Installer.py