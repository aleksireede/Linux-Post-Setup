#!/bin/bash
if ! command -v lolcat &> /dev/null
then
    /usr/bin/env python3 -m pip install lolcat
fi
if ! command -v yt-dlp &> /dev/null
then
/usr/bin/env python3 -m pip install yt-dlp
fi
/usr/bin/env python3 -m pip install python-telegram-bot -U --pre
/usr/bin/env python3 -m pip install websockets GitPython wakeonlan pathlib2 requests
/usr/bin/env python3 -m pip install --user --upgrade pynvim
export PATH="$PATH:/home/$USER/.local/bin/"
chmod +x ./Installer.py
./Installer.py
cd ..
rm -rf ./Linux-First-Setup