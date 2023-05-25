import subprocess
import pathlib2
import requests
import os
import program_commands
import program_common
import Program_Main
linux_distro = program_commands.linux_distro
username = program_commands.username

debian_package_directory = pathlib2.Path(pathlib2.Path.cwd(), "pkgs", "debian")
debian_pkgs = program_commands.text_filter(
    open(pathlib2.Path(debian_package_directory, "debian.txt"), "r").read())

class apt:
    def update():
        subprocess.run(["sudo", "apt", "-q", "update"], check=True,
                       text=True, input=program_commands.password)

    def upgrade():
        subprocess.run(["sudo", "apt", "-q", "--assume-yes",
                        "upgrade"], check=True, text=True, input=program_commands.password)

    def autoremove():
        subprocess.run(["sudo", "apt", "-qq", "autoremove"],
                       check=True, text=True, input=program_commands.password)

    def install(apps: list[str]):
        apt_install_list = ["sudo", "apt", "--assume-yes", "install"]
        apt_install_list.extend(apps)
        subprocess.run(apt_install_list, check=True, text=True,
                       input=program_commands.password)


def debian():
    if not pathlib2.Path("/home"+username+".cargo/bin").exists:
        subprocess.run("curl https://sh.rustup.rs -sSf | sh", shell=True)
        os.environ["PATH"] += ":/home/" + \
            username+"/.cargo/bin"
    apt.update()
    apt.upgrade()
    apt.install(["gnupg", "curl", "apt-transport-https", "software-properties-common"])
    debian_pkgs.extend(program_common.common_pkgs)
    apt.install(debian_pkgs)
    apt.autoremove()
