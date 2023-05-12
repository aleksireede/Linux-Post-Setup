#!/usr/bin/env python3
import subprocess
import pathlib2
import program_commands


def start():
    android_pkgs_install()
    subprocess.run(
        "chsh -s /bin/zsh", shell=True)


android_package_directory = pathlib2.Path(
    pathlib2.Path.cwd(), "pkgs", "android")
android_pkgs = program_commands.text_filter(
    open(pathlib2.Path(android_package_directory, "android.txt"), "r").read())


class apt:
    def update():
        subprocess.run(["apt", "-q", "update"], check=True,
                       text=True)

    def upgrade():
        subprocess.run(["apt", "-q", "--assume-yes",
                        "upgrade"], check=True, text=True)

    def autoremove():
        subprocess.run(["apt", "-qq", "autoremove"],
                       check=True, text=True)

    def install(apps: list[str]):
        apt_install_list = ["apt", "--assume-yes", "install"]
        apt_install_list.extend(apps)
        subprocess.run(apt_install_list, check=True, text=True)


def android_pkgs_install():
    apt.update()
    apt.upgrade()
    apt.install(["gnupg", "curl", "apt-transport-https"])
    apt.install(android_pkgs)
    apt.autoremove()
