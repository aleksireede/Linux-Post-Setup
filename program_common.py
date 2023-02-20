import subprocess
import pathlib2
import requests
import program_commands
import Program_Main
import shutil
import git
import typing


librewolf_conf_text = open(pathlib2.Path(
    pathlib2.Path.cwd(), "text", "keepassxc_browser_plugin.json")).read()
character_blacklist = [" ", "\\", "/", "\"",
                       "\'", ",", ".", "\n", "\r", "\t", "\b", "\f"]
zshrc = pathlib2.Path("/home", program_commands.get_user(), ".zshrc")
bashrc = pathlib2.Path("/home", program_commands.get_user(), ".bashrc")
alias_file = open(pathlib2.Path("./text/alias.txt"), "r").read()
zsh_aliases = pathlib2.Path(
    "/home", program_commands.get_user(), ".zsh_aliases")
bash_aliases = pathlib2.Path(
    "/home", program_commands.get_user(), ".bash_aliases")
zsh_plugin_path = pathlib2.Path(
    "/home", program_commands.get_user(), ".oh-my-zsh/custom/plugins")


class systemd_util:
    def start(service_name: str):
        '''Starts a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "start", service_name+".service"])

    def start_user(service_name: str):
        '''Starts a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "start", service_name +
                        "@"+program_commands.get_user()+".service"])

    def enable(service_name: str):
        '''Enables a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "enable", service_name+".service"])

    def enable_user(service_name: str):
        '''Enables a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "enable", service_name +
                        "@"+program_commands.get_user()+".service"])

    def disable(service_name: str):
        '''Disables a systemd service. default is system service'''
        subprocess.run(
            ["sudo", "systemctl", "disable", service_name+".service"])

    def disable_user(service_name: str):
        '''Disables a systemd service. default is system service'''
        subprocess.run(["sudo", "systemctl", "disable", service_name +
                        "@"+program_commands.get_user()+".service"])

    def stop(service_name: str):
        '''Stops a systemd system service.'''
        subprocess.run(
            ["sudo", "systemctl", "stop", service_name+".service"])

    def stop_user(service_name: str):
        '''Stops a systemd user service.'''
        subprocess.run(["sudo", "systemctl", "stop", service_name +
                        "@"+program_commands.get_user()+".service"])


def package_filter(package_list):
    package_list = package_list.replace("\n", " ")
    package_list_complete = []
    for app in package_list.split(" "):
        if any(app) in character_blacklist:
            continue
        package_list_complete.append(app)
    return package_list_complete


common_packages = package_filter(
    open("./packages/common/common.txt", "r").read())
common_desktop_packages = package_filter(
    open("./packages/common/common_desktop.txt", "r").read())
common_gnome_packages = package_filter(
    open("./packages/common/common_gnome.txt", "r").read())


def noto_emoji_apple():
    open(pathlib2.Path(r"/tmp/NotoColorEmoji.ttf"), "wb").write(requests.get(
        "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false").content)
    if pathlib2.Path("/usr/share/fonts/truetype").exists():
        if pathlib2.Path("/usr/share/fonts/truetype/NotoColorEmoji.ttf").exists():
            subprocess.run(
                ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"], check=True, text=True)
        subprocess.run(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                        "/usr/share/fonts/truetype/NotoColorEmoji.ttf"], check=True, text=True)
    elif pathlib2.Path("/usr/share/fonts/noto").exists():
        if pathlib2.Path("/usr/share/fonts/noto/NotoColorEmoji.ttf").exists():
            subprocess.run(
                ["sudo", "rm", "/usr/share/fonts/noto/NotoColorEmoji.ttf"], check=True, text=True)
        subprocess.run(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                        "/usr/share/fonts/noto/NotoColorEmoji.ttf"], check=True, text=True)


def install_zsh_plugin(name):
    git.Repo.clone_from("https://github.com/zsh-users/" +
                        name+".git",  pathlib2.Path(zsh_plugin_path, name))


def oh_my_zsh():
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
                                 program_commands.get_user()+'"\nprompt_context(){}\n')
    program_commands.text_modify(
        zshrc, "if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi")
    program_commands.text_modify(
        bashrc, "if [ -f ~/.bash_aliases ]; then\n. ~/.bash_aliases\nfi")
    program_commands.text_modify(
        zsh_aliases, "#!/usr/bin/env zsh\n"+alias_file)
    program_commands.text_modify(
        bash_aliases, "#!/usr/bin/env bash\n"+alias_file)


def amogus_cowfile():
    if pathlib2.Path("/usr/share/cows/amogus.cow").exists() or pathlib2.Path("/usr/share/cowsay/cows/amogus.cow").exists():
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


def install_custom_git(url: str, directory: pathlib2.Path, command: list):
    '''Install a program from git url with a custom supplied command list'''
    git.Repo.clone_from(url, directory)
    if any(isinstance(x, typing.List) for x in command):
        for x in command:
            subprocess.run(x, cwd=directory, check=True, text=True)
    else:
        subprocess.run(command, cwd=directory, check=True, text=True)
    shutil.rmtree(directory)


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


def change_display_manager():
    systemd_util.disable("display-manager")
    if Program_Main.desktop_environment == "gnome":
        systemd_util.enable("gdm")
    elif Program_Main.desktop_environment == "kde":
        systemd_util.enable("sddm")


def librewolf_keepassxc_browser_fix():
    librewolf_conf_dir = pathlib2.Path("/home", program_commands.get_user(), ".librewolf",
                                       "native-messaging-hosts")
    librewolf_conf_json = pathlib2.Path(
        librewolf_conf_dir, "org.keepassxc.keepassxc_browser.json")
    if not librewolf_conf_dir.exists():
        librewolf_conf_dir.mkdir(parents=True, exist_ok=True)
    program_commands.text_modify(librewolf_conf_json, librewolf_conf_text)


def Main():
    program_commands.clear_screen()
    amogus_cowfile()
    program_commands.clear_screen()
    oh_my_zsh()
    install_custom_git("https://github.com/trakBan/ipfetch.git",
                       pathlib2.Path(pathlib2.Path.cwd(), "ipfecth"), ["sudo", "sh", "setup.sh"])
    if Program_Main.is_server_apps:
        return
    systemd_util.start("bluetooth")
    systemd_util.start_user("syncthing")
    change_display_manager()
    if Program_Main.desktop_environment == "gnome":
        gnome_volume_steps()
    program_commands.clear_screen()
    noto_emoji_apple()
    program_commands.clear_screen()
    install_oreo_cursors()
