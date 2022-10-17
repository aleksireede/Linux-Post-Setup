#!/usr/bin/env python3
import subprocess
import pathlib2
import shutil
from tkinter import Pack
import requests
import git
bash_URL = "https://pastebin.com/raw/7B7hmX2a"
zsh_URL = "https://pastebin.com/raw/t5rM9rxa"
bash_response = requests.get(bash_URL)
zsh_response = requests.get(zsh_URL)
bashrc = pathlib2.Path(pathlib2.Path.home(), r"/.bashrc")
zshrc = pathlib2.Path(pathlib2.Path.home(), r"/.zshrc")
welcome_text = open("welcome_text.txt", "r").read()
arch_packages = open("./packages/arch.txt", "r").read()
common_packages = open("./packages/common.txt", "r").read()
debian_packages = open("./packages/debian.txt", "r").read()
flatpak_packages = open("./packages/flatpak.txt", "r").read()
welcome_print = subprocess.run(["lolcat"], input=welcome_text, text=True, )
while True:
    subprocess.call(["clear"])
    welcome_print
    yes_no = input("Do you wish to run the script? [Y/n]:")
    if yes_no.lower() == "y" or yes_no.lower() == "yes":
        break
    elif yes_no.lower() == "n" or yes_no.lower() == "no":
        exit(1)
    else:
        print("Please answer yes or no!")
subprocess.call(["clear"])


def is_tool(name):
    # check if program exists
    return shutil.which(name) is not None


def findtext(text, file):
    data = file.read_text()
    if text in data:
        return "Text already found:"+text
    data = data+text
    file.write_text(data)
    return "Text written"


def replacetext(search_text, replace_text, file):
    # replace text in a file
    data = file.read_text()
    if not search_text in data:
        return "String Not found:"+search_text
    data = data.replace(search_text, replace_text)
    file.write_text(data)
    return "Text replaced"


# only for Arch linux because it uses different package manager than debian etc
if pathlib2.Path("/etc/arch-release").is_file():
    # Install aur helper if not already installed. this will make installing programs easier
    if not is_tool("paru"):
        executable = ""
        if not is_tool("yay"):
            while True:
                yn = input(
                    "Do you want to install paru instead of yay? (y/N):")
                if yn.lower() == "y":
                    executable = "paru"
                    break
                elif yn.lower() == "n":
                    executable = "yay"
                    break
                else:
                    print("Please answer yes or no!")
        else:
            executable = "paru"
        subprocess.call(["sudo", "pacman", "-S", "--needed", "base-devel"])
        subprocess.call(
            ["git", "clone", "https://aur.archlinux.org/"+executable+".git"])
        subprocess.call(["makepkg", "-si"],
                        cwd=pathlib2.Path(pathlib2.Path.cwd(), executable))
        shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), executable),
                      ignore_errors=False, onerror=None)
    # Install all applications games etc
    subprocess.call(["paru", "-Suy", "--needed", "-quiet",
                    "\\", arch_packages, common_packages])
    # modify pacman config
    if pathlib2.Path(r"/etc/pacman.conf").exists():
        filepath = pathlib2.Path(r"/etc/pacman.conf")
        print(replacetext("#[multilib]", "[multilib]", filepath))
        print(replacetext("#Include = /etc/pacman.d/mirrorlist",
              "Include = /etc/pacman.d/mirrorlist", filepath))
        print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5", filepath))
        print(replacetext("#Color", "Color", filepath))

# Install Flatpak packages (universal)
subprocess.call(["flatpak", "install", "flathub", flatpak_packages])
if bashrc.exists():
    print(
        findtext("if [ -f ~/.bash_aliases ]; then\n. ~/.bash_aliases\nfi", bashrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.bash_aliases"),
         "wb").write(bash_response.content)
elif zshrc.exists():
    print(
        findtext("if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi", zshrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases"),
         "wb").write(zsh_response.content)

# Install Doas (Sudo alternative) which is more secure and compact
#subprocess.call(["chmod", "+x", "./utils/doas.sh"])
# subprocess.call(["./utils/doas.sh"])

if not is_tool("doas"):
    doaspath = pathlib2.Path(pathlib2.Path.cwd(), "doas")
    git.Repo.clone_from("https://github.com/slicer69/doas.git",
                        doaspath)
    subprocess.call(["make"],
                    cwd=doaspath)
    subprocess.call(["sudo", "make", "install"],
                    cwd=doaspath)
    open(pathlib2.Path(r"/usr/local/etc/doas.conf")
         ).write(requests.get("https://pastebin.com/raw/EK6hud2S").content)
    subprocess.call(["sudo", "chmod", "0400", "/usr/local/etc/doas.conf"])
    subprocess.call(["sudo", "chown", "root:root", "/usr/local/etc/doas.conf"])
    subprocess.call(["sudo", "dos2unix", "/usr/local/etc/doas.conf"])
    shutil.rmtree(doaspath)
