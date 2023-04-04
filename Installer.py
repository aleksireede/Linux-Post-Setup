#!/usr/bin/env python3
import Program_Main
import subprocess
import os
import pathlib2
import git
import shutil
from program_commands import get_username, os_check, is_tool

username = get_username()
os.environ["PATH"] += ":/home/"+username+"/.local/bin/:/home/" + \
    username+"/.local/share/gem/ruby/3.0.0/bin/"
lolcat_binary_path = pathlib2.Path("/home", username, ".local/bin/lolcat")
lolcat_temp_path = pathlib2.Path("/tmp/lolcat")
system = os_check()


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
                   cwd=pathlib2.Path(lolcat_temp_path, "bin"), check=True, text=True)
    shutil.copyfile(pathlib2.Path(lolcat_temp_path,
                    "bin", "lolcat"), lolcat_binary_path)
    subprocess.run(["sudo", "chmod", "+x", lolcat_binary_path],
                   check=True, text=True)
    shutil.rmtree(lolcat_temp_path)
Program_Main.main()
