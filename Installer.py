#!/usr/bin/env python3
import Program_Main
import subprocess
import os
from program_commands import get_username, os_check, is_tool

username = get_username()
os.environ["PATH"] += ":/home/"+username+"/.local/bin/:/home/" + \
    ":/home/"+username+"/.local/share/gem/ruby/3.0.0/bin/"
system = os_check()


if not is_tool("lolcat") and not is_tool("gem"):
    if system == "arch":
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "ruby"])
    elif system == "debian":
        subprocess.run(["sudo", "apt", "-y", "install", "rubygems"],
                       check=True, text=True)


if not is_tool("lolcat"):
    subprocess.run(["gem", "install", "lolcat"], check=True, text=True)
Program_Main.main()
