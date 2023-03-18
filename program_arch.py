import subprocess
import pathlib2
import shutil
import git
import program_commands
import program_common
import Program_Main
import typing

arch_packages = program_common.package_filter(
    open("./pkgs/arch/arch.txt", "r").read())
arch_pulseaudio_packages = program_common.package_filter(
    open("./pkgs/arch/arch_pulseaudio.txt", "r").read())
arch_pipewire_packages = program_common.package_filter(
    open("./pkgs/arch/arch_pipewire.txt", "r").read())
arch_desktop_packages = program_common.package_filter(
    open("./pkgs/arch/arch_desktop.txt", "r").read())
arch_kde_packages = program_common.package_filter(
    open("./pkgs/arch/arch_kde.txt", "r").read())
arch_gnome_packages = program_common.package_filter(
    open("./pkgs/arch/arch_gnome.txt", "r").read())
arch_wayland_packages = program_common.package_filter(
    open("./pkgs/arch/arch_wayland.txt", "r").read())
pacman_conf = pathlib2.Path(r"/etc/pacman.conf")
paru_path = pathlib2.Path(pathlib2.Path.cwd(), "paru")


def arch():
    pacman_config()
    check_for_aur_helper()
    arch_packages_install()


class pacman:
    def update_db():
        subprocess.run(["sudo", "pacman", "-Sy", "--needed",
                       "--noconfirm", "archlinux-keyring"], check=True, text=True)

    def install(packages: list):
        arch_app_list = ["paru", "-S", "--needed"]
        if any(isinstance(x, typing.List) for x in packages):
            for package in packages:
                arch_app_list.extend(package)
        else:
            arch_app_list.extend(packages)
        subprocess.run(arch_app_list, check=True, text=True)

    def update():
        subprocess.run(["paru", "-Suy", "--noconfirm"], check=True, text=True)

    def autoremove():
        subprocess.run("pacman -Qtdq | sudo pacman -Rns -", shell=True)

    def remove(packages: list):
        arch_app_remove = ["paru", "-R", "--noconfirm"]
        if any(isinstance(x, typing.List) for x in packages):
            for package in packages:
                arch_app_remove.extend(package)
        else:
            arch_app_remove.extend(packages)
        try:
            subprocess.run(arch_app_remove, check=True, text=True)
        except:
            return


def arch_packages_install():
    pacman.update_db()
    install_list = [arch_packages, program_common.common_packages,
                    program_common.common_gnome_packages]
    uninstall_list = []
    if Program_Main.audio_environment == "pipewire":
        uninstall_list.append(arch_pulseaudio_packages)
    elif Program_Main.audio_environment == "pulseaudio":
        uninstall_list.append(arch_pipewire_packages)
    if not Program_Main.is_server_apps:
        install_list.extend(
            [arch_desktop_packages, arch_wayland_packages, program_common.common_desktop_packages])
        if Program_Main.desktop_environment == "kde":
            install_list.append(arch_kde_packages)
            uninstall_list.append(arch_gnome_packages)
        elif Program_Main.desktop_environment == "gnome":
            uninstall_list.append(arch_kde_packages)
            install_list.append(arch_gnome_packages)
    pacman.remove(uninstall_list)
    pacman.install(install_list)
    pacman.update()
    pacman.autoremove()
    program_commands.clear_screen()


def check_for_aur_helper():
    if program_commands.is_tool("paru") or program_commands.is_tool("yay"):
        return
    subprocess.run(["sudo", "pacman", "-S", "--needed", "--noconfirm",
                   "base-devel"], check=True, text=True)
    git.Repo.clone_from("https://aur.archlinux.org/paru.git", paru_path)
    subprocess.run(["makepkg", "-si"], cwd=paru_path, check=True, text=True)
    shutil.rmtree(paru_path, ignore_errors=False, onerror=None)
    program_commands.clear_screen()


def pacman_config():
    if not pacman_conf.exists() or Program_Main.is_server_apps:
        return
    subprocess.run(["sudo", "chmod", "777", pacman_conf],
                   check=True, text=True)
    program_commands.text_modify(
        pacman_conf, "#[multilib]\n#Include = /etc/pacman.d/mirrorlist", "[multilib]\nInclude = /etc/pacman.d/mirrorlist")
    program_commands.text_modify(
        pacman_conf, "#ParallelDownloads=5", "ParallelDownloads=5")
    program_commands.text_modify(pacman_conf, "#Color", "Color")
    subprocess.run(["sudo", "chmod", "644", pacman_conf],
                   check=True, text=True)
    program_commands.clear_screen()
