#!/usr/bin/env python3
import Program_Main
import sys
import subprocess
import pkg_resources
from program_commands import get_user, os_check, is_tool
import os
import pathlib2
import git
import shutil

lolcat_binary_path = pathlib2.Path("/usr/bin/lolcat")
lolcat_temp_path = pathlib2.Path("/tmp/lolcat")

system = os_check()
required = {"yt-dlp", "websockets",
            "GitPython", "pathlib2", "requests"}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if not is_tool("lolcat") and not is_tool("gem"):
    if system == "arch":
        subprocess.run(["sudo", "pacman", "-S", "--noconfirm", "ruby"])
    elif system == "debian":
        subprocess.run(["sudo", "apt", "-y", "install", "rubygems"],
                       check=True, text=True)
if not is_tool("lolcat"):
    git.Repo.clone_from(
        "https://github.com/aleksireede/lolcat.git", lolcat_temp_path)
    subprocess.run(["sudo", "gem", "install", "lolcat"],
                   cwd=pathlib2.Path(lolcat_temp_path, "bin"))
    pathlib2.Path(lolcat_temp_path, "bin", "lolcat").rename(lolcat_binary_path)
    shutil.rmtree(lolcat_temp_path)

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
os.environ["PATH"] += ":/home/"+get_user()+"/.local/bin/:/home/" + \
    get_user()+"/.local/share/gem/ruby/3.0.0/bin/"
Program_Main.main()
