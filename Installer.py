#!/usr/bin/env python3
import Program_Main
import subprocess
import os
from program_commands import get_username, os_check, is_tool, password

username = get_username()
local_bin_path = os.path.join("/home", username, ".local", "bin")
ruby_bin_path = os.path.join(
    "/home", username, ".local", "share", "gem", "ruby", "3.0.0", "bin")
os.environ["PATH"] += f":{local_bin_path}:{ruby_bin_path}"
system = os_check()


if not is_tool("lolcat"):
    if system == "arch":
        subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm", "archlinux-keyring"],
                       check=True, text=True, input=password)
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "lolcat"],
                       check=True, text=True, input=password)
    elif system == "debian":
        subprocess.run(["sudo", "apt", "-y", "install", "rubygems"],
                       check=True, text=True, input=password)
        subprocess.run(["sudo", "gem", "install", "lolcat"],
                       check=True, text=True, input=password)
    elif system == "android":
        subprocess.run(["pkg", "install", "ruby"], check=True, text=True)
        subprocess.run(["gem", "install", "lolcat"], check=True, text=True)
Program_Main.main()
