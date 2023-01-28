import subprocess
import pathlib2
import shutil
import git
import program_commands
import program_common

arch_packages = open("./packages/arch.txt", "r").read()
arch_packages = arch_packages.replace("\n", " ")
arch_packages_remove = open("./packages/arch_remove.txt", "r").read()
arch_packages_remove = arch_packages_remove.replace("\n", " ")
arch_desktop_packages = open("./packages/arch_desktop.txt", "r").read()
arch_desktop_packages = arch_desktop_packages.replace("\n", " ")
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
    subprocess.run(["sudo", "pacman", "-Sy", "--needed", "archlinux-keyring"],
                   check=True, text=True)
    arch_app_list = ["paru", "-Suy", "--needed"]
    arch_app_remove = ["paru" "-R"]
    arch_app_remove.extend(arch_packages_remove)
    if not program_commands.is_server():
        arch_app_list.extend(program_common.package_filter(arch_desktop_packages))
        arch_app_list.extend(program_common.package_filter(program_common.common_desktop_packages))
    arch_app_list.extend(program_common.package_filter(arch_packages))
    arch_app_list.extend(program_common.package_filter(
        program_common.common_packages))
    subprocess.run(arch_app_remove,check=True,text=True)
    subprocess.run(
        arch_app_list, check=True, text=True)
    subprocess.run("pacman -Qtdq | sudo pacman -Rns -", shell=True)


def check_for_aur_helper():
    if program_commands.is_tool("paru") or program_commands.is_tool("yay"):
        return
    subprocess.run(["sudo", "pacman", "-S", "--needed",
                   "base-devel"], check=True, text=True)
    git.Repo.clone_from("https://aur.archlinux.org/paru.git", paru_path)
    subprocess.run(["makepkg", "-si"], cwd=paru_path, check=True, text=True)
    shutil.rmtree(paru_path, ignore_errors=False, onerror=None)


def pacman_config():
    if not pacman_conf.exists() or program_commands.is_server():
        return
    subprocess.run(["sudo", "chmod", "777", pacman_conf],
                   check=True, text=True)
    print(program_commands.replace_text("#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
          "[multilib]\nInclude = /etc/pacman.d/mirrorlist", pacman_conf))
    print(program_commands.replace_text(
        "#ParallelDownloads=5", "ParallelDownloads=5", pacman_conf))
    print(program_commands.replace_text("#Color", "Color", pacman_conf))
    subprocess.run(["sudo", "chmod", "644", pacman_conf],
                   check=True, text=True)
