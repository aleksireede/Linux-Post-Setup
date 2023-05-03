import subprocess
import pathlib2
import shutil
import git
import program_commands
import program_common
import Program_Main
import typing

arch_package_directory = pathlib2.Path(pathlib2.Path.cwd(), "pkgs", "arch")
arch_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch.txt"), "r").read())
arch_pulseaudio_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_pulseaudio.txt"), "r").read())
arch_pipewire_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_pipewire.txt"), "r").read())
arch_desktop_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_desktop.txt"), "r").read())
arch_kde_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_kde.txt"), "r").read())
arch_gnome_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_gnome.txt"), "r").read())
arch_wayland_pkgs = program_commands.text_filter(
    open(pathlib2.Path(arch_package_directory, "arch_wayland.txt"), "r").read())

pacman_conf = pathlib2.Path(r"/etc/pacman.conf")
paru_path = pathlib2.Path(pathlib2.Path.cwd(), "paru")


def arch():
    pacman_config()
    check_for_aur_helper()
    arch_pkgs_install()


class pacman:
    def update_db():
        subprocess.run(["sudo", "pacman", "-Sy", "--needed",
                       "--noconfirm", "archlinux-keyring"], check=True, text=True)

    def install(pkgs: list):
        arch_app_list = ["paru", "-S", "--needed"]
        if any(isinstance(x, typing.List) for x in pkgs):
            for package in pkgs:
                arch_app_list.extend(package)
        else:
            arch_app_list.extend(pkgs)
        try:
            subprocess.run(arch_app_list, check=True, text=True)
        except:
            print("Error when installing packages aborting...")
            program_commands.press_enter_to_continue()
            exit()

    def update():
        subprocess.run(["paru", "-Suy", "--noconfirm"], check=True, text=True)

    def autoremove():
        subprocess.run("pacman -Qtdq | sudo pacman -Rns -", shell=True)

    def remove(pkgs: list):
        arch_app_remove = ["paru", "-R", "--noconfirm"]
        if any(isinstance(x, typing.List) for x in pkgs):
            for package in pkgs:
                arch_app_remove.extend(package)
        else:
            arch_app_remove.extend(pkgs)
        try:
            subprocess.run(arch_app_remove, check=True, text=True)
        except:
            return


def arch_pkgs_install():
    pacman.update_db()
    install_list = [arch_pkgs, program_common.common_pkgs]
    uninstall_list = []
    if Program_Main.audio_environment == "pipewire":
        uninstall_list.append(arch_pulseaudio_pkgs)
        install_list.append(arch_pipewire_pkgs)
    elif Program_Main.audio_environment == "pulseaudio":
        install_list.append(arch_pulseaudio_pkgs)
        uninstall_list.append(arch_pipewire_pkgs)
    if not Program_Main.is_server_install_type:
        install_list.extend(
            [arch_desktop_pkgs, arch_wayland_pkgs, program_common.common_desktop_pkgs])
        if Program_Main.desktop_environment == "kde":
            install_list.append(arch_kde_pkgs)
            uninstall_list.append(arch_gnome_pkgs)
            uninstall_list.append(program_common.common_gnome_pkgs)
        elif Program_Main.desktop_environment == "gnome":
            uninstall_list.append(arch_kde_pkgs)
            install_list.append(arch_gnome_pkgs)
            install_list.append(program_common.common_gnome_pkgs)
    pacman.remove(uninstall_list)
    pacman.install(install_list)
    pacman.update()
    pacman.autoremove()
    program_commands.clear_screen()


def check_for_aur_helper():
    if program_commands.is_tool("paru"):
        return
    pacman.update_db()
    subprocess.run(["sudo", "pacman", "-S", "--needed", "--noconfirm",
                   "base-devel"], check=True, text=True)
    git.Repo.clone_from("https://aur.archlinux.org/paru.git", paru_path)
    subprocess.run(["makepkg", "-si"], cwd=paru_path, check=True, text=True)
    shutil.rmtree(paru_path, ignore_errors=False, onerror=None)
    program_commands.clear_screen()


def pacman_config():
    program_commands.text_modify(
        pacman_conf, "#[multilib]\n#Include = /etc/pacman.d/mirrorlist", "[multilib]\nInclude = /etc/pacman.d/mirrorlist")
    program_commands.text_modify(
        pacman_conf, "#ParallelDownloads = 5", "ParallelDownloads = 8")
    program_commands.text_modify(pacman_conf, "#Color", "Color")
    program_commands.clear_screen()
