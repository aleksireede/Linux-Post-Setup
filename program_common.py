import subprocess
import pathlib2
import requests
import program_commands
import Program_Main
import shutil
import git
import typing

zshrc = pathlib2.Path("/home", program_commands.get_user(), ".zshrc")
bashrc = pathlib2.Path("/home", program_commands.get_user(), ".bashrc")
alias_file = open(pathlib2.Path("./text/alias.txt"), "r").read()
zsh_aliases = pathlib2.Path(
    "/home", program_commands.get_user(), ".zsh_aliases")
bash_aliases = pathlib2.Path(
    "/home", program_commands.get_user(), ".bash_aliases")
zsh_plugin_path = pathlib2.Path(
    "/home", program_commands.get_user(), ".oh-my-zsh/custom/plugins")

common_packages = open("./packages/common.txt", "r").read()
common_packages = common_packages.replace("\n", " ")
common_desktop_packages = open("./packages/common_desktop.txt", "r").read()
common_desktop_packages = common_desktop_packages.replace("\n", " ")
character_blacklist = ["'", "", "\\", "/", "\"", ",", "."]


def package_filter(package_list):
    package_list_complete = []
    for app in package_list.split(" "):
        if app in character_blacklist:
            continue
        package_list_complete.append(app)
    return package_list_complete


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
    # open(bashrc, "w").write("exec zsh")


def amogus_cowfile():
    if pathlib2.Path("/usr/share/cows/amogus.cow").exists() or pathlib2.Path("/usr/share/cowsay/cows/amogus.cow").exists():
        return
    if pathlib2.Path("/usr/share/cows").exists():
        pathlib2.Path(pathlib2.Path.cwd(), "text", "amogus.cow").rename(
            pathlib2.Path("/usr/share/cows/amogus.cow"))
    elif pathlib2.Path("/usr/share/cowsay/cows/amogus.cow").exists():
        pathlib2.Path(pathlib2.Path.cwd(), "text", "amogus.cow").rename(
            pathlib2.Path("/usr/share/cowsay/cows/amogus.cow"))


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


def enable_service_systemd(serviceName: str, isUserService: bool):
    if isUserService:
        enable_service_list: list[str] = ["sudo", "systemctl", "enable",
                                          serviceName+"@"+program_commands.get_user()+".service"]
        start_service_list: list[str] = ["sudo", "systemctl", "start",
                                         serviceName+"@"+program_commands.get_user()+".service"]
    else:
        enable_service_list: list[str] = ["sudo", "systemctl",
                                          "enable", serviceName+".service"]
        start_service_list: list[str] = ["sudo", "systemctl",
                                         "start", serviceName+".service"]
    subprocess.run(enable_service_list)
    subprocess.run(start_service_list)


def install_custom_git(url: str, directory: pathlib2.Path, command: list):
    git.Repo.clone_from(url, directory)
    if any(isinstance(x, typing.List) for x in command):
        for x in command:
            subprocess.run(x, check=True, text=True)
    else:
        subprocess.run(command, check=True, text=True)
    shutil.rmtree(directory)


def check_gsettings():
    if not program_commands.is_tool("gsettings"):
        return
    try:
        subprocess.check_output(
            "gsettings list-schemas | grep org.gnome.settings-daemon.plugins.media-keys", shell=True)
    except:
        return
    subprocess.run(["gsettings", "set", "org.gnome.settings-daemon.plugins.media-keys",
                    "volume-step", "1"], check=True, text=True)


def Main():
    check_gsettings()
    # install_custom_git("https://github.com/trakBan/ipfetch.git",
    #                  pathlib2.Path(pathlib2.Path.cwd(), "ipfecth"), ["sudo", "sh", "setup.sh"])
    enable_service_systemd("syncthing", True)
    if Program_Main.is_server:
        return
    program_commands.clear_screen()
    noto_emoji_apple()
    program_commands.clear_screen()
    install_oreo_cursors()
    program_commands.clear_screen()
    oh_my_zsh()
    program_commands.clear_screen()
    amogus_cowfile()
    program_commands.clear_screen()
