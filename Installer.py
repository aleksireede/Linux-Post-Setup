#!/usr/bin/env python3
<<<<<<< HEAD
import subprocess
welcome_text = open("welcome_text.txt", "r").read()
welcome_print = subprocess.run(["lolcat"], input=welcome_text, text=True, )
welcome_print
while True:
=======
from re import A
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

while True:
    subprocess.call(["clear"])
    subprocess.run(["lolcat"], input=welcome_text, text=True, )
>>>>>>> 2106bd62a46d7ef72af7e4d6c20c872c01c81e70
    yes_no = input("Do you wish to run the script? [Y/n]:")
    if yes_no.lower() == "y" or yes_no.lower() == "yes":
        break
    elif yes_no.lower() == "n" or yes_no.lower() == "no":
        exit(1)
    else:
        print("Please answer yes or no!")
<<<<<<< HEAD
subprocess.run(["python3", "-m", "pip", "install",
               "pathlib2", "websockets", "yt-dlp"], text=True)
=======


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

def oreo_cursors():
    git.Repo.clone_from("https://github.com/varlesh/oreo-cursors.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["ruby", "generator/convert.rb"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["make", "build"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["sudo", "make", "install"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["clear"])
def asus_linux():
    git.Repo.clone_from("https://gitlab.com/asus-linux/asusctl.git",
                    pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["make"], cwd=pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["sudo", "make", "install"],
                cwd=pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["clear"])


# only for Arch linux because it uses different package manager than debian etc
if pathlib2.Path("/etc/arch-release").is_file():
    subprocess.call(["clear"])
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
    arch_app_list = ["paru", "-Suy", "--needed", "-quiet"]
    arch_packages = arch_packages.replace("\n", "")
    arch_packages = arch_packages.replace("'", "")
    common_packages = common_packages.replace("\n", "")
    common_packages = common_packages.replace("'", "")
    for app in arch_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    for app in common_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    subprocess.call(arch_app_list, shell=True)
    subprocess.call(["clear"])
    # modify pacman config
    if pathlib2.Path(r"/etc/pacman.conf").exists():
        filepath = pathlib2.Path(r"/etc/pacman.conf")
        print(replacetext("#[multilib]", "[multilib]", filepath))
        print(replacetext("#Include = /etc/pacman.d/mirrorlist",
              "Include = /etc/pacman.d/mirrorlist", filepath))
        print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5", filepath))
        print(replacetext("#Color", "Color", filepath))

# Debian only
elif pathlib2.Path("/etc/lsb-release").is_file() or pathlib2.Path("/etc/debian_version").is_file() or pathlib2.Path("/etc/linuxmint/info").is_file():
    subprocess.call(["clear"])
    subprocess.call(["chmod", "+x", "./utils/debian_sources.sh",
                    "&&", "./utils/debian_sources.sh"])
    subprocess.call(["sudo", "apt", "-qq", "update"])
    subprocess.call(["sudo", "apt", "-qq", "--assume-yes", "-y",
                    "install", "\\", debian_packages, common_packages])
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.call(["sudo", "apt", "qq", "install",
                    "--assume-yes", "y", "./steam.deb"])
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
    # Install fastfetch
    fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")
    git.Repo.clone_from(
        "https://github.com/LinusDierheimer/fastfetch.git", fastfetchpath)
    pathlib2.Path(fastfetchpath, "build").mkdir(parents=True, exist_ok=True)
    subprocess.call(["cmake", ".."], cwd=pathlib2.Path(fastfetchpath, "build"))
    subprocess.call(["cmake", "--build", ".", "-j$(nproc)", "--target", "fastfetch",
                    "--target", "flashfetch"], cwd=pathlib2.Path(fastfetchpath, "build"))
    shutil.rmtree(fastfetchpath)
    subprocess.call(["sudo", "apt", "-qq", "update"])
    subprocess.call(["sudo", "apt", "-qq", "upgrade"])
    subprocess.call(["sudo", "apt", "-qq", "autoremove"])
    subprocess.call(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"])

# Install Flatpak packages (universal)
subprocess.call(["clear"])
for app in flatpak_packages.split(" "):
    subprocess.call(["flatpak", "install", "flathub", app])

# shell aliases
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

# Install Doas (sudo alternative)
if not is_tool("doas"):
    doaspath = pathlib2.Path(pathlib2.Path.cwd(), "doas")
    git.Repo.clone_from("https://github.com/slicer69/doas.git",
                        doaspath)
    subprocess.call(["make"],
                    cwd=doaspath)
    subprocess.call(["sudo", "make", "install"],
                    cwd=doaspath)
    open(pathlib2.Path(r"/usr/local/etc/doas.conf"), "wb"
         ).write(requests.get("https://pastebin.com/raw/EK6hud2S").content)
    subprocess.call(["sudo", "chmod", "0400", "/usr/local/etc/doas.conf"])
    subprocess.call(["sudo", "chown", "root:root", "/usr/local/etc/doas.conf"])
    subprocess.call(["sudo", "dos2unix", "/usr/local/etc/doas.conf"])
    shutil.rmtree(doaspath)

# Make nemo default file manager
subprocess.call(["xdg-mime", "default", "nemo.desktop",
                "inode/directory", "application/x-gnome-saved-search"])

# Arduino cli
open(pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz"), "wb").write(requests.get(
    "https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz").content)
subprocess.call(["sudo", "tar", "xf", "arduino-cli.tgz",
                "-C", "/usr/local/bin", "arduino-cli"])
pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz").unlink()

# Notocolor emoji apple
if pathlib2.Path(r"/usr/share/fonts/truetype/").exists():
    if pathlib2.Path(r"/usr/share/fonts/truetype/NotoColorEmoji.ttf").exists():
        subprocess.call(
            ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"])
    open(pathlib2.Path(r"/tmp/NotoColorEmoji.ttf"), "wb").write(requests.get(
        "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false").content)
    subprocess.call(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                    "/usr/share/fonts/noto/NotoColorEmoji.ttf"])
    subprocess.call(["clear"])
elif pathlib2.Path(r"/usr/share/fonts/noto/").exists():
    if pathlib2.Path(r"/usr/share/fonts/noto/NotoColorEmoji.ttf").exists():
        subprocess.call(
            ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"])
    open(pathlib2.Path(r"/tmp/NotoColorEmoji.ttf"), "wb").write(requests.get(
        "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false").content)
    subprocess.call(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                    "/usr/share/fonts/noto/NotoColorEmoji.ttf"])
    subprocess.call(["clear"])

# Install Mangohud
git.Repo.clone_from("https://github.com/flightlessmango/MangoHud.git",
                    pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
subprocess.call(["chmod", "+x", "./build.sh"],
                cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
subprocess.call(["./build.sh", "build"],
                cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
subprocess.call(["./build.sh", "install"],
                cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
subprocess.call(["clear"])

# Install asus-linux
while True:
    subprocess.call(["clear"])
    subprocess.call(
        ["lolcat"], input="Do you want to compile and install asus-linux? (y/N):", text=True)
    yesno = input()
    if yesno.lower() == "n":
        exit()
    elif yesno.lower() == "y":
        asus_linux()
        break
    else:
        print("Please answer yes or no!")


# Oreo Cursors
while True:
    subprocess.call(["clear"])
    subprocess.call(
        ["lolcat"], input="Do you want to compile and install oreo cursor? (y/N):", text=True)
    yesno = input()
    if yesno.lower() == "n":
        exit()
    elif yesno.lower() == "y":
        oreo_cursors()
        break
    else:
        print("Please answer yes or no!")
>>>>>>> 2106bd62a46d7ef72af7e4d6c20c872c01c81e70
