import subprocess
import pathlib2
import requests
import os
import program_commands
import program_common
import Program_Main

debian_packages = program_common.package_filter(
    open("./packages/debian/debian.txt", "r").read())
debian_gnome_packages = program_common.package_filter(
    open("./packages/debian/debian_gnome.txt", "r").read())
debian_desktop_packages = program_common.package_filter(
    open("./packages/debian/debian_desktop.txt", "r").read())
flatpak_packages = program_common.package_filter(
    open("./packages/debian/flatpak.txt", "r").read())
fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")


def debian():
    program_commands.clear_screen()
    debian_packages_install()
    if Program_Main.is_server_apps:
        return
    program_commands.clear_screen()
    debian_steam()
    program_commands.clear_screen()
    flatpak()
    program_commands.clear_screen()
    if not program_commands.is_tool("mangohud"):
        debian_mangohud()
        program_commands.clear_screen()


def flatpak():
    for app in flatpak_packages.split(" "):
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


class apt:
    def update():
        subprocess.run(["sudo", "apt", "-q", "update"], check=True, text=True)

    def upgrade():
        subprocess.run(["sudo", "apt", "-q", "--assume-yes",
                        "upgrade"], check=True, text=True)

    def add_repo(repo: str):
        subprocess.run(["sudo", "add-apt-repository", repo],
                       check=True, text=True)

    def autoremove():
        subprocess.run(["sudo", "apt", "-qq", "autoremove"],
                       check=True, text=True)

    def install(apps: list[str]):
        apt_install_list = ["sudo", "apt", "-q", "--assume-yes", "install"]
        apt_install_list = apt_install_list.extend(apps)
        subprocess.run(apt_install_list, check=True, text=True)


def debian_packages_install():
    subprocess.run("curl https://sh.rustup.rs -sSf | sh", shell=True)
    os.environ["PATH"] += ":/home/"+program_commands.get_user()+"/.cargo/bin"
    subprocess.run(
        "bash <(wget -qO- https://raw.githubusercontent.com/Heroic-Games-Launcher/HeroicGamesLauncher/main/rauldipeas.sh)", shell=True)
    download_file_from_url("/etc/apt/trusted.gpg.d/ani-cli.asc",
                           "https://Wiener234.github.io/ani-cli-ppa/KEY.gpg")
    download_file_from_url("/etc/apt/sources.list.d/ani-cli-debian.list",
                           "https://Wiener234.github.io/ani-cli-ppa/ani-cli-debian.list")
    download_file_from_url("/usr/share/keyrings/syncthing-archive-keyring.gpg",
                           "https://syncthing.net/release-key.gpg")
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/syncthing.list"),
                                 "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable")
    download_file_from_url("/usr/share/keyrings/grapejuice-archive-keyring.gpg",
                           "https://gitlab.com/brinkervii/grapejuice/-/raw/master/ci_scripts/signing_keys/public_key.gpg")
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/grapejuice.list"),
                                 'deb [signed-by=/usr/share/keyrings/grapejuice-archive-keyring.gpg] https://brinkervii.gitlab.io/grapejuice/repositories/debian/ universal main')
    subprocess.run("curl -fsSL https://packagecloud.io/filips/FirefoxPWA/gpgkey | gpg --dearmor | sudo tee /usr/share/keyrings/firefoxpwa-keyring.gpg > /dev/null", shell=True)
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/firefoxpwa.list"),
                                 "deb [signed-by=/usr/share/keyrings/firefoxpwa-keyring.gpg] https://packagecloud.io/filips/FirefoxPWA/any any main")
    subprocess.run("wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg", shell=True)
    program_commands.text_modify(pathlib2.Path("/etc/apt/sources.list.d/vscodium.list"),
                                 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://download.vscodium.com/debs vscodium main')
    apt.add_repo("universe")
    apt.add_repo("multiverse")
    apt.add_repo("ppa:cappelikan/ppa")
    apt.add_repo("ppa:flexiondotorg/mangohud")
    subprocess.run(["sudo", "dpkg", "--add-architecture",
                   "i386"], check=True, text=True)
    apt.update()
    apt.upgrade()
    apt.install(["gnupg", "curl", "apt-transport-https"])
    if not Program_Main.is_server_apps:
        debian_packages.extend(debian_desktop_packages)
        debian_packages.extend(program_common.common_desktop_packages)
        subprocess.run(
            ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"], check=True, text=True)
    debian_packages.extend(program_common.common_packages)
    debian_packages.extend(program_common.common_gnome_packages)
    debian_packages.extend(debian_gnome_packages)
    apt.install(debian_packages)
    apt.autoremove()


def download_file_from_url(output_file, content_url):
    program_commands.text_modify(pathlib2.Path(
        output_file), str(requests.get(content_url).content))


def debian_mangohud():
    program_common.install_custom_git("https://github.com/flightlessmango/MangoHud.git", pathlib2.Path(pathlib2.Path.cwd(
    ), "Mangohud"), [["chmod", "+x", "./build.sh"], ["./build.sh", "build"], ["./build.sh", "install"]])


def debian_steam():
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "-qq", "install",
                    "--assume-yes", "-y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
