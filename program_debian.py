import subprocess
import pathlib2
import requests
import os
import program_commands
import program_common
import Program_Main
linux_distro = program_commands.linux_distro
username = program_commands.username

debian_pkgs = program_common.package_filter(
    open("./pkgs/debian/debian.txt", "r").read())
debian_gnome_pkgs = program_common.package_filter(
    open("./pkgs/debian/debian_gnome.txt", "r").read())
debian_desktop_pkgs = program_common.package_filter(
    open("./pkgs/debian/debian_desktop.txt", "r").read())
debian_flatpak_pkgs = program_common.package_filter(
    open("./pkgs/debian/flatpak.txt", "r").read())
fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")


def debian():
    debian_pkgs_install()
    if Program_Main.is_server_install_type:
        return
    debian_steam()
    flatpak()
    if not program_commands.is_tool("mangohud"):
        debian_mangohud()


def flatpak():
    subprocess.run(["flatpak", "remote-add", "--if-not-exists", "flathub",
                   "https://flathub.org/repo/flathub.flatpakrepo"], check=True, text=True)
    for app in debian_flatpak_pkgs:
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)
    program_commands.clear_screen()


class apt:
    def update():
        subprocess.run(["sudo", "apt", "-q", "update"], check=True, text=True)

    def upgrade():
        subprocess.run(["sudo", "apt", "-q", "--assume-yes",
                        "upgrade"], check=True, text=True)

    def add_repo(repo: str):
        try:
            repo_list = subprocess.check_output(
                ["sudo", "grep", "-h", "^deb", "/etc/apt/sources.list", "/etc/apt/sources.list.d/*"])
        except subprocess.CalledProcessError:
            repo_list = []
        if repo in repo_list:
            return
        try:
            subprocess.run(["sudo", "add-apt-repository", repo],
                           check=True, text=True)
        except subprocess.CalledProcessError:
            subprocess.run(["sudo", "apt-get", "install",
                           "software-properties-common"], check=True, text=True)
            # needs possibly fixing

    def autoremove():
        subprocess.run(["sudo", "apt", "-qq", "autoremove"],
                       check=True, text=True)

    def install(apps: list[str]):
        apt_install_list = ["sudo", "apt", "--assume-yes", "install"]
        apt_install_list.extend(apps)
        subprocess.run(apt_install_list, check=True, text=True)

    def aria2_install(url):
        subprocess.run(["aria2c", "-o", "temp.deb", url],
                       cwd=pathlib2.Path(pathlib2.Path.cwd(), "temp"), check=True, text=True)
        apt.install("temp.deb")
        os.remove(pathlib2.Path(pathlib2.Path.cwd(), "temp", "temp.deb"))


def debian_pkgs_install():
    if not pathlib2.Path("/home"+username+".cargo/bin").exists:
        subprocess.run("curl https://sh.rustup.rs -sSf | sh", shell=True)
        os.environ["PATH"] += ":/home/" + \
            username+"/.cargo/bin"
    download_file_from_url("/etc/apt/trusted.gpg.d/ani-cli.asc",
                           "https://Wiener234.github.io/ani-cli-ppa/KEY.gpg")
    download_file_from_url("/etc/apt/sources.list.d/ani-cli-debian.list",
                           "https://Wiener234.github.io/ani-cli-ppa/ani-cli-debian.list")
    download_file_from_url("/etc/apt/trusted.gpg.d/microsoft.asc",
                           "https://pkgs.microsoft.com/keys/microsoft.asc")
    subprocess.run("curl -fsSL https://packagecloud.io/filips/FirefoxPWA/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/firefoxpwa-keyring.gpg > /dev/null", shell=True)
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/firefoxpwa.list"),
                                 "deb [signed-by=/usr/share/keyrings/firefoxpwa-keyring.gpg] https://packagecloud.io/filips/FirefoxPWA/any any main")
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/vscode.list"),
                                 'deb [arch=amd64] https://pkgs.microsoft.com/repos/vscode stable main')
    apt.add_repo("universe")
    apt.add_repo("multiverse")
    apt.add_repo("ppa:nextcloud-devs/client")
    apt.add_repo("ppa:mozillateam/ppa")
    apt.add_repo("ppa:yt-dlp/stable")
    subprocess.run(["sudo", "dpkg", "--add-architecture",
                   "i386"], check=True, text=True)
    apt.update()
    apt.upgrade()
    apt.install(["gnupg", "curl", "apt-transport-https"])
    if not Program_Main.is_server_install_type:
        debian_pkgs.extend(debian_desktop_pkgs)
        debian_pkgs.extend(program_common.common_desktop_pkgs)
        debian_pkgs.extend(program_common.common_gnome_pkgs)
        debian_pkgs.extend(debian_gnome_pkgs)
        apt.aria2_install(
            "https://discord.com/api/download?platform=linux&format=deb")
    debian_pkgs.extend(program_common.common_pkgs)
    apt.install(debian_pkgs)
    apt.autoremove()


def download_file_from_url(output_file, content_url):
    if pathlib2.Path(output_file).exists():
        return
    subprocess.run(["sudo", "touch", output_file], text=True, check=True)
    subprocess.run(["sudo", "chmod", "777", output_file],
                   text=True, check=True)
    program_commands.text_modify(pathlib2.Path(
        output_file), requests.get(content_url).text)


def debian_mangohud():
    program_common.install_custom_git("https://github.com/flightlessmango/MangoHud.git", pathlib2.Path(pathlib2.Path.cwd(
    ), "Mangohud"), [["chmod", "+x", "./build.sh"], ["./build.sh", "build"], ["./build.sh", "install"]])


def debian_steam():
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "-qq", "install",
                    "--assume-yes", "-y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
