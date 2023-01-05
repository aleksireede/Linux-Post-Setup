import subprocess
import pathlib2
import shutil
import requests
import git
import getpass
import sys
import program_commands
import program_common

debian_packages = open("./packages/debian.txt", "r").read()
flatpak_packages = open("./packages/flatpak.txt", "r").read()
fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")

def debian():
    clear_screen()
    debian_steam()
    clear_screen()
    debian_packages_install()
    clear_screen()
    clear_screen()
    flatpak()
    if not is_tool("mangohud"):
        if yes_no_check("Do you want to compile and install mangohud"):
            debian_mangohud()
            clear_screen()


def flatpak():
    for app in flatpak_packages.split(" "):
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


def debian_packages_install():
    subprocess.run(["chmod", "+x", "./utils/debian_sources.sh"],
                   check=True, text=True)
    subprocess.run(["./utils/debian_sources.sh"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "update"], check=True, text=True)
    debian_app_list = ["sudo", "apt", "-qq", "--assume-yes", "-y"]
    debian_app_list.extend(program_common.package_filter(debian_packages))
    debian_app_list.extend(program_common.package_filter(program_common.common_packages))
    subprocess.run(
        debian_app_list, check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "upgrade"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "autoremove"], check=True, text=True)
    subprocess.run(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"], check=True, text=True)


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
    subprocess.run(["sudo", "apt", "-qq", "install",
                    "--assume-yes", "-y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()

