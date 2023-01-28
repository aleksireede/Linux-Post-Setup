#!/usr/bin/env python3
import sys
import subprocess
import pkg_resources
from program_commands import get_user,os_check
import os

os_check()
required = {"lolcat", "yt-dlp", "websockets",
            "GitPython", "pathlib2", "requests"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
os.environ["PATH"] += ":/home/"+get_user()+"/.local/bin/"
import Program_Main
Program_Main.main()
