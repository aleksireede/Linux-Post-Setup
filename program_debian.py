import subprocess
import pathlib2
import shutil
import requests
import git
import program_commands
import program_common
import Program_Main

debian_packages = open("./packages/debian.txt", "r").read()
debian_packages = debian_packages.replace("\n", " ")
debian_desktop_packages = open("./packages/debian_desktop.txt", "r").read()
debian_desktop_packages = debian_desktop_packages.replace("\n", " ")
flatpak_packages = open("./packages/flatpak.txt", "r").read()
flatpak_packages = flatpak_packages.replace("\n", " ")
fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")


def debian():
    program_commands.clear_screen()
    debian_packages_install()
    if Program_Main.is_server:
        return
    program_commands.clear_screen()
    debian_steam()
    program_commands.clear_screen()
    flatpak()
    program_commands.clear_screen()
    if not program_commands.is_tool("mangohud"):
        if program_commands.yes_no_check("Do you want to compile and install mangohud"):
            debian_mangohud()
            program_commands.clear_screen()


def flatpak():
    for app in flatpak_packages.split(" "):
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


def debian_packages_install():
    subprocess.run(["chmod", "+x", "./utils/debian_sources.sh"],
                   check=True, text=True)
    subprocess.run(["./utils/debian_sources.sh"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-q", "update"], check=True, text=True)
    debian_app_list = ["sudo", "apt", "-q", "--assume-yes", "-y", "install"]
    debian_app_list.extend(program_common.package_filter(debian_packages))
    if not Program_Main.is_server:
        debian_app_list.extend(
            program_common.package_filter(debian_desktop_packages))
        debian_app_list.extend(program_common.package_filter(
            program_common.common_desktop_packages))
    debian_app_list.extend(program_common.package_filter(
        program_common.common_packages))
    subprocess.run(
        debian_app_list, check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "upgrade"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "autoremove"], check=True, text=True)
    subprocess.run(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"], check=True, text=True)
    subprocess.run(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" --unattended', shell=True)


def debian_mangohud():
    program_common.install_custom_git("https://github.com/flightlessmango/MangoHud.git", pathlib2.Path(pathlib2.Path.cwd(
    ), "Mangohud"), [["chmod", "+x", "./build.sh"], ["./build.sh", "build"], ["./build.sh", "install"]])


def debian_steam():
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "-qq", "install",
                    "--assume-yes", "-y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
