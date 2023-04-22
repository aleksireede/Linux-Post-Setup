import subprocess
import pathlib2
import requests
import program_commands
import Program_Main
import shutil
import git
import tempfile
import typing
linux_distro = program_commands.linux_distro
username = program_commands.username


librewolf_conf_text = open(pathlib2.Path(
    pathlib2.Path.cwd(), "text", "keepassxc_browser_plugin.json")).read()
zshrc = pathlib2.Path("/home", username, ".zshrc")
bashrc = pathlib2.Path("/home", username, ".bashrc")
alias_file = open(pathlib2.Path("./text/alias.txt"), "r").read()
zsh_aliases = pathlib2.Path(
    "/home", username, ".zsh_aliases")
bash_aliases = pathlib2.Path(
    "/home", username, ".bash_aliases")
zsh_plugin_path = pathlib2.Path(
    "/home", username, ".oh-my-zsh/custom/plugins")


class systemd_util:
    def start(service_name: str):
        '''Starts a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "start", service_name+".service"])

    def start_user(service_name: str):
        '''Starts a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "start", service_name +
                        "@"+username+".service"])

    def enable(service_name: str):
        '''Enables a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "enable", service_name+".service"])

    def enable_user(service_name: str):
        '''Enables a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "enable", service_name +
                        "@"+username+".service"])

    def disable(service_name: str):
        '''Disables a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "disable", service_name+".service"])

    def disable_user(service_name: str):
        '''Disables a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "disable", service_name +
                        "@"+username+".service"])

    def stop(service_name: str):
        '''Stops a systemd system service.'''
        subprocess.run(
            ["sudo", "systemctl", "stop", service_name+".service"])

    def stop_user(service_name: str):
        '''Stops a systemd user service.'''
        subprocess.run(["sudo", "systemctl", "stop", service_name +
                        "@"+username+".service"])


common_pkgs = program_commands.text_filter(
    open("./pkgs/common/common.txt", "r").read())
common_desktop_pkgs = program_commands.text_filter(
    open("./pkgs/common/common_desktop.txt", "r").read())
common_gnome_pkgs = program_commands.text_filter(
    open("./pkgs/common/common_gnome.txt", "r").read())
common_flatpak_pkgs = program_commands.text_filter(
    open("./pkgs/common/flatpak.txt", "r").read())


def flatpak():
    subprocess.run(["flatpak", "remote-add", "--if-not-exists", "flathub",
                   "https://flathub.org/repo/flathub.flatpakrepo"], check=True, text=True)
    for app in common_flatpak_pkgs:
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


def noto_emoji_apple():
    response = requests.get(
        "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false")
    response.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(response.content)
    if program_commands.is_tool("fc-cache"):
        font_dir = "/usr/share/fonts/truetype"
    else:
        font_dir = "/usr/share/fonts/noto"
    font_path = pathlib2.Path(font_dir, "NotoColorEmoji.ttf")
    if font_path.exists():
        subprocess.run(["sudo", "rm", str(font_path)], check=True, text=True)
    subprocess.run(["sudo", "mv", temp_file.name, str(font_path)],
                   check=True, text=True)
    program_commands.clear_screen()


def install_zsh_plugin(name):
    git.Repo.clone_from("https://github.com/zsh-users/" +
                        name+".git",  pathlib2.Path(zsh_plugin_path, name))
    program_commands.clear_screen()


def shell_customize():
    if zsh_plugin_path.exists():
        return
    subprocess.run(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended', shell=True)
    install_zsh_plugin("zsh-syntax-highlighting")
    install_zsh_plugin("zsh-autosuggestions")
    program_commands.text_modify(
        zshrc, "plugins=(git)", "plugins=(\ngit\nzsh-autosuggestions\nzsh-syntax-highlighting\n)")
    program_commands.text_modify(
        zshrc, 'ZSH_THEME="robbyrussell"', 'ZSH_THEME="agnoster"')
    program_commands.text_modify(zshrc, 'DEFAULT_USER="' +
                                 username+'"\nprompt_context(){}\n')
    program_commands.text_modify(
        zshrc, "if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi")
    program_commands.text_modify(
        bashrc, "if [ -f ~/.bash_aliases ]; then\n. ~/.bash_aliases\nfi")
    program_commands.text_modify(
        zsh_aliases, "#!/usr/bin/env zsh\n"+alias_file)
    program_commands.text_modify(
        bash_aliases, "#!/usr/bin/env bash\n"+alias_file)
    program_commands.clear_screen()


def amogus_cowfile():
    if pathlib2.Path("/usr/share/cows/amogus.cow").exists() or pathlib2.Path("/usr/share/cowsay/cows/amogus.cow").exists() or pathlib2.Path("/usr/local/share/cowsay/cows/amogus.cow").exists():
        return
    if pathlib2.Path("/usr/share/cows").exists():
        subprocess.run(["sudo", "chmod", "777", "/usr/share/cows/"],
                       check=True, text=True)
        shutil.copyfile(pathlib2.Path(pathlib2.Path.cwd(), "text",
                        "amogus.cow"), pathlib2.Path("/usr/share/cows/amogus.cow"))
    elif pathlib2.Path("/usr/share/cowsay/cows/").exists():
        subprocess.run(["sudo", "chmod", "777", "/usr/share/cowsay/cows"],
                       check=True, text=True)
        shutil.copyfile(pathlib2.Path(pathlib2.Path.cwd(
        ), "text", "amogus.cow"), pathlib2.Path("/usr/share/cowsay/cows/amogus.cow"))
    elif pathlib2.Path("/usr/local/share/cowsay/cows").exists():
        subprocess.run(["sudo", "chmod", "777",
                       "/usr/local/share/cowsay/cows"], check=True, text=True)
        shutil.copyfile(pathlib2.Path(pathlib2.Path.cwd(), "text", "amogus.cow"),
                        pathlib2.Path("/usr/local/share/cowsay/cows/amogus.cow"))
    program_commands.clear_screen()


def install_oreo_cursors():
    if pathlib2.Path("/usr/share/icons/oreo_blue_cursors/cursor.theme").exists():
        return  # exit if cursors already exist
    git.Repo.clone_from("https://github.com/varlesh/oreo-cursors.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.run(["ruby", "generator/convert.rb"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["make", "build"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["sudo", "make", "install"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    program_commands.clear_screen()


def install_custom_git(url: str, directory: pathlib2.Path, command: list):
    '''Install a program from git url with a custom supplied command list'''
    git.Repo.clone_from(url, directory)
    if any(isinstance(x, typing.List) for x in command):
        for x in command:
            subprocess.run(x, cwd=directory, check=True, text=True)
    else:
        subprocess.run(command, cwd=directory, check=True, text=True)
    shutil.rmtree(directory)
    program_commands.clear_screen()


def gnome_volume_steps():
    if not program_commands.is_tool("gsettings"):
        return
    try:
        subprocess.check_output(
            "gsettings list-schemas | grep org.gnome.settings-daemon.plugins.media-keys", shell=True)
    except:
        return
    subprocess.run(["gsettings", "set", "org.gnome.settings-daemon.plugins.media-keys",
                    "volume-step", "1"], check=True, text=True)
    program_commands.clear_screen()


def change_display_manager():
    systemd_util.disable("display-manager")
    if Program_Main.desktop_environment == "gnome":
        if linux_distro == "debian":
            subprocess.run(["sudo", "dpkg-reconfigure", "gdm3"],
                           check=True, text=True)
        systemd_util.enable("gdm")
    elif Program_Main.desktop_environment == "kde":
        if linux_distro == "debian":
            subprocess.run(["sudo", "dpkg-reconfigure", "sddm"],
                           check=True, text=True)
        systemd_util.enable("sddm")
    program_commands.clear_screen()


def librewolf_keepassxc_browser_fix():
    librewolf_conf_dir = pathlib2.Path("/home", username, ".librewolf",
                                       "native-messaging-hosts")
    librewolf_conf_json = pathlib2.Path(
        librewolf_conf_dir, "org.keepassxc.keepassxc_browser.json")
    if not librewolf_conf_dir.exists():
        librewolf_conf_dir.mkdir(parents=True, exist_ok=True)
    program_commands.text_modify(librewolf_conf_json, librewolf_conf_text)
    program_commands.clear_screen()


def remove_snap_packagaes():
    snaps = subprocess.Popen(["snap", "list"], stdout=subprocess.PIPE)
    snap_list_1 = subprocess.run(
        ["awk", "!/^Name|^core|^bare|^snapd/ {print $1}"], stdin=snaps.stdout, stdout=subprocess.PIPE)
    snap_list_2 = subprocess.run(
        ["awk", "/^bare/ {print $1}"], stdin=snaps.stdout, stdout=subprocess.PIPE)
    snap_list_3 = subprocess.run(
        ["awk", "/^core/ {print $1}"], stdin=snaps.stdout, stdout=subprocess.PIPE)
    snap_list_4 = subprocess.run(
        ["awk", "/^snapd/ {print $1}"], stdin=snaps.stdout, stdout=subprocess.PIPE)
    snap_remove_list = ["sudo", "snap", "remove"]
    # we need to check that the lists are not empty and then fiter the list out of unwanted charatcters like "\n"
    if snap_list_1.stdout.decode():
        snap_remove_list.extend(
            program_commands.text_filter(snap_list_1.stdout.decode()))
    if snap_list_2.stdout.decode():
        snap_remove_list.extend(
            program_commands.text_filter(snap_list_2.stdout.decode()))
    if snap_list_3.stdout.decode():
        snap_remove_list.extend(
            program_commands.text_filter(snap_list_3.stdout.decode()))
    if snap_list_4.stdout.decode():
        snap_remove_list.extend(
            program_commands.text_filter(snap_list_4.stdout.decode()))
    if not snap_list_1.stdout.decode() and not snap_list_2.stdout.decode() and not snap_list_3.stdout.decode() and not snap_list_4.stdout.decode():
        return  # we don't have any snap pkgs so we don't remove something we don't have
    subprocess.run(snap_remove_list, check=True, text=True)
    program_commands.clear_screen()


def snap_nuke():
    if not program_commands.is_tool("snap"):
        return
    remove_snap_packagaes()
    volume_list = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    snap_vol_list = subprocess.check_output(
        ["awk", "/snap/ {print $6}"], stdin=volume_list.stdout)
    for vol in snap_vol_list:
        subprocess.run(["sudo", "umount", vol])
    if linux_distro == "arch":
        subprocess.run(["sudo", "pacman", "-Rns", "snapd"],
                       check=True, text=True)
    elif linux_distro == "debian":
        program_commands.text_modify(pathlib2.Path("/etc/apt/preferences.d/nosnap.pref"), open(
            pathlib2.Path(pathlib2.Path.cwd(), "text", "nosnap.pref")).read())
        program_commands.text_modify(pathlib2.Path("/etc/apt/preferences.d/firefox-no-snap"), open(
            pathlib2.Path(pathlib2.Path.cwd(), "text", "firefox-no-snap.pref")).read())
        subprocess.run(["sudo", "apt", "purge", "snapd"],
                       check=True, text=True)
    program_commands.clear_screen()


def Main():
    snap_nuke()
    amogus_cowfile()
    shell_customize()
    if not program_commands.is_tool("ipfetch"):
        install_custom_git("https://github.com/trakBan/ipfetch.git",
                           pathlib2.Path(pathlib2.Path.cwd(), "tmp", "ipfecth"), ["sudo", "sh", "setup.sh"])
    if not program_commands.is_tool("cowsay"):
        install_custom_git("https://github.com/cowsay-org/cowsay.git", pathlib2.Path(
            pathlib2.Path.cwd(), "tmp", "cowsay"), ["sudo", "make", "install"])
    if Program_Main.is_server_install_type:
        return
    flatpak()
    systemd_util.start("bluetooth")
    systemd_util.start_user("syncthing")
    change_display_manager()
    if Program_Main.desktop_environment == "gnome":
        gnome_volume_steps()
    noto_emoji_apple()
    install_oreo_cursors()
    subprocess.run("localectl --no-convert set-x11-keymap fi", shell=True)
