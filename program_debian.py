import subprocess
import pathlib2
import shutil
import requests
import git
import getpass
import sys
from program_commands import *
from program_common import *

debian_packages = open("./packages/debian.txt", "r").read()
flatpak_packages = open("./packages/flatpak.txt", "r").read()
fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")


def debian():
    clear_screen()
    flatpak()
    clear_screen()
    debian_steam()
    clear_screen()
    debian_arduino_cli()
    clear_screen()
    debian_fastfetch()
    clear_screen()
    debian_packages_install()
    clear_screen()
    if not is_tool("mangohud"):
        if yes_no_check("Do you want to compile and install mangohud"):
            debian_mangohud()
            clear_screen()


def flatpak():
    for app in flatpak_packages.split(" "):
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


def debian_packages_installs():
    subprocess.run(["chmod", "+x", "./utils/debian_sources.sh"],
                   check=True, text=True)
    subprocess.run(["./utils/debian_sources.sh"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "update"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "--assume-yes", "-y",
                    "install", "\\", debian_packages, common_packages], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "upgrade"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "autoremove"], check=True, text=True)
    subprocess.run(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"], check=True, text=True)

# possibly needs fix


def debian_arduino_cli():
    open(pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz"), "wb").write(requests.get(
        "https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz").content)
    subprocess.run(["tar", "xf", "arduino-cli.tgz",
                    "-C", "/usr/local/bin", "arduino-cli"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz").unlink()


def debian_fastfetch():
    git.Repo.clone_from(
        "https://github.com/LinusDierheimer/fastfetch.git", fastfetchpath)
    pathlib2.Path(fastfetchpath, "build").mkdir(parents=True, exist_ok=True)
    subprocess.run(["cmake", ".."], cwd=pathlib2.Path(
        fastfetchpath, "build"), check=True, text=True)
    subprocess.run(["cmake", "--build", ".", "-j$(nproc)", "--target", "fastfetch",
                    "--target", "flashfetch"], cwd=pathlib2.Path(fastfetchpath, "build"), check=True, text=True)
    shutil.rmtree(fastfetchpath)


def debian_mangohud():
    git.Repo.clone_from("https://github.com/flightlessmango/MangoHud.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.run(["chmod", "+x", "./build.sh"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    subprocess.run(["./build.sh", "build"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    subprocess.run(["./build.sh", "install"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(),
                  "Mangohud"))


def debian_steam():
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "qq", "install",
                    "--assume-yes", "y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
