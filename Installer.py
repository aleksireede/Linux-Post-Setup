#!/usr/bin/env python3
import Program_Main
import sys
import subprocess
import pkg_resources
from program_commands import get_user, os_check, is_tool
import os

system = os_check()
required = {"yt-dlp", "websockets",
            "GitPython", "pathlib2", "requests"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if not is_tool("lolcat") and not is_tool("gem"):
    if system == "arch":
        subprocess.run(["sudo", "pacman", "-S", "ruby"])
    elif system == "debian":
        subprocess.run(["sudo", "apt", "install", "rubygems"],
                       check=True, text=True)
if not is_tool("lolcat"):
    pass

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
os.environ["PATH"] += ":/home/"+get_user()+"/.local/bin/:/home/"+get_user()+"/.local/share/gem/ruby/3.0.0/bin/"
Program_Main.main()
