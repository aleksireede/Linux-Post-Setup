import subprocess
import pathlib2
import shutil
import requests
import git
import getpass
import program_commands
import program_common

arch_packages = open("./packages/arch.txt", "r").read()
arch_packages = arch_packages.replace("\n", " ")
pacman_conf = pathlib2.Path(r"/etc/pacman.conf")
paru_path = pathlib2.Path(pathlib2.Path.cwd(), "paru")


def arch():
    program_commands.clear_screen()
    pacman_config()
    program_commands.clear_screen()
    check_for_aur_helper()
    program_commands.clear_screen()
    arch_packages_install()
    program_commands.clear_screen()


def arch_packages_install():
    subprocess.run(["sudo", "pacman", "-Sy", "archlinux-keyring"],
                   check=True, text=True)
    arch_app_list = ["paru", "-Suy", "--needed"]
    arch_app_list.extend(program_common.package_filter(arch_packages))
    arch_app_list.extend(program_common.package_filter(program_common.common_packages))
    subprocess.run(
        arch_app_list, check=True, text=True)
    pacman_remove_orphans = subprocess.Popen("sudo pacman -Qtdq"], stdout=subprocess.PIPE)
    arch_orphaned_packages = pacman_remove_orphans.stdout.read()
    subprocess.run(["sudo", "pacman", "-Rns"], check=True, text=True, input=arch_orphaned_packages)


def check_for_aur_helper():
    if program_commands.is_tool("paru") or is_tool("yay"):
        return
    subprocess.run(["pacman", "-S", "--needed",
                   "base-devel"], check=True, text=True)
    git.Repo.clone_from("https://aur.archlinux.org/paru.git", paru_path)
    subprocess.run(["makepkg", "-si"], cwd=paru_path, check=True, text=True)
    shutil.rmtree(paru_path, ignore_errors=False, onerror=None)


def pacman_config():
    if not pacman_conf.exists():
        return
    subprocess.run(["sudo", "chmod", "777", pacman_conf],
                   check=True, text=True)
    print(program_commands.replacetext("#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
          "[multilib]\nInclude = /etc/pacman.d/mirrorlist", pacman_conf))
    print(program_commands.replacetext(
        "#ParallelDownloads=5", "ParallelDownloads=5", pacman_conf))
    print(program_commands.replacetext("#Color", "Color", pacman_conf))
    subprocess.run(["sudo", "chmod", "644", pacman_conf],
                   check=True, text=True)
