import subprocess
import pathlib2
import shutil
import requests
import git
import getpass
import program_commandss
import program_common

arch_packages = open("./packages/arch.txt", "r").read()
arch_packages = arch_packages.replace("\n", " ")
pacman_conf = pathlib2.Path(r"/etc/pacman.conf")
paru_path = pathlib2.Path(pathlib2.Path.cwd(), "paru")


def arch():
    clear_screen()
    pacman_config()
    clear_screen()
    check_for_aur_helper()
    clear_screen()
    arch_packages_install()
    clear_screen()
    press_enter_to_continue()


def arch_packages_install():
    arch_app_list = ["paru", "-Suy", "--needed"]
    for app in arch_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    for app in common_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    subprocess.run(
        arch_app_list, check=True, text=True)


def check_for_aur_helper():
    if is_tool("paru") or is_tool("yay"):
        return
    subprocess.run(["pacman", "-S", "--needed",
                   "base-devel"], check=True, text=True)
    git.Repo.clone_from("https://aur.archlinux.org/paru.git", paru_path)
    subprocess.run(["makepkg", "-si"], cwd=paru_path, check=True, text=True)
    shutil.rmtree(paru_path, ignore_errors=False, onerror=None)


def pacman_config():
    if not pacman_conf.exists():
        return
    # subprocess.run([ "chmod", "777", pacman_conf],
    #                check=True, text=True)
    print(replacetext("#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
          "[multilib]\nInclude = /etc/pacman.d/mirrorlist", pacman_conf))
    print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5", pacman_conf))
    print(replacetext("#Color", "Color", pacman_conf))
    # subprocess.run([ "chmod", "644", pacman_conf],
    #                check=True, text=True)
