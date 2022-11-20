#!/usr/bin/env python3
import subprocess
import pathlib2
import shutil
import requests
import git
import getpass

zsh_URL = "https://pastebin.com/raw/t5rM9rxa"
zsh_response = requests.get(zsh_URL)
zshrc = pathlib2.Path(pathlib2.Path.home(), r"/.zshrc")
welcome_text = open("welcome_text.txt", "r").read()
arch_packages = open("./packages/arch.txt", "r").read()
common_packages = open("./packages/common.txt", "r").read()
debian_packages = open("./packages/debian.txt", "r").read()
flatpak_packages = open("./packages/flatpak.txt", "r").read()
arch_packages = arch_packages.replace("\n", " ")
common_packages = common_packages.replace("\n", " ")
pacman_conf = pathlib2.Path(r"/etc/pacman.conf")

while True:
    subprocess.run(["clear"], check=True, text=True)
    subprocess.run(["lolcat"], input=welcome_text, check=True, text=True)
    subprocess.run(
        ["lolcat"], input="Do you wish to run the script?\n(y/N):", check=True, text=True)
    yes_no = input("")
    if yes_no.lower() == "y" or yes_no.lower() == "yes":
        break
    elif yes_no.lower() == "n" or yes_no.lower() == "no":
        exit(1)
    else:
        print("Please answer yes or no!")


def is_tool(name):
    # check if program exists
    return shutil.which(name) is not None


def findtext(text, file):
    data = file.read_text()
    if text in data:
        return "Text already found:"+text
    data = data+text
    file.write_text(data)
    return "Text written"


def replacetext(search_text, replace_text, file):
    # replace text in a file
    data = file.read_text()
    if not search_text in data:
        return "String Not found:"+search_text
    data = data.replace(search_text, replace_text)
    file.write_text(data)
    return "Text replaced"


def oreo_cursors():
    git.Repo.clone_from("https://github.com/varlesh/oreo-cursors.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.run(["ruby", "generator/convert.rb"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["make", "build"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["sudo", "make", "install"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    input("Press Enter to continue...")
    subprocess.run(["clear"], check=True, text=True)


def check_for_aur_helper():
    if is_tool("paru") or is_tool("yay"):
        return
    subprocess.run(["sudo", "pacman", "-S", "--needed",
                   "base-devel"], check=True, text=True)
    subprocess.run(
        ["git", "clone", "https://aur.archlinux.org/paru.git"], check=True, text=True)
    subprocess.run(["makepkg", "-si"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "paru"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "paru"),
                  ignore_errors=False, onerror=None)


def pacman_config():
    if not pacman_conf.exists():
        return
    subprocess.run(["sudo", "chmod", "777", pacman_conf],
                   check=True, text=True)
    print(replacetext("#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
          "[multilib]\nInclude = /etc/pacman.d/mirrorlist", pacman_conf))
    print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5", pacman_conf))
    print(replacetext("#Color", "Color", pacman_conf))
    subprocess.run(["sudo", "chmod", "644", pacman_conf],
                   check=True, text=True)


def mangohud():
    git.Repo.clone_from("https://github.com/flightlessmango/MangoHud.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.run(["chmod", "+x", "./build.sh"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    subprocess.run(["./build.sh", "build"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    subprocess.run(["./build.sh", "install"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(),
                  "Mangohud"))
    subprocess.run(["clear"], check=True, text=True)

# Notocolor emoji apple


def noto_emoji_apple():
    open(pathlib2.Path(r"/tmp/NotoColorEmoji.ttf"), "wb").write(requests.get(
        "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false").content)
    if pathlib2.Path(r"/usr/share/fonts/truetype/").exists():
        if pathlib2.Path(r"/usr/share/fonts/truetype/NotoColorEmoji.ttf").exists():
            subprocess.run(
                ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"], check=True, text=True)
        subprocess.run(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                        "/usr/share/fonts/truetype/NotoColorEmoji.ttf"], check=True, text=True)
    elif pathlib2.Path(r"/usr/share/fonts/noto/").exists():
        if pathlib2.Path(r"/usr/share/fonts/noto/NotoColorEmoji.ttf").exists():
            subprocess.run(
                ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"], check=True, text=True)
        subprocess.run(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                        "/usr/share/fonts/noto/NotoColorEmoji.ttf"], check=True, text=True)
    subprocess.run(["clear"])


def oh_my_zsh():
    zsh_alias = pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases")
    subprocess.run(
        ["sh", "-c", '"$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"'], check=True, text=True)
    git.Repo.clone_from("https://github.com/zsh-users/zsh-syntax-highlighting.git",
                        "/home/$USER/.oh-my-zsh/doas/plugins/zsh-syntax-highlighting")
    git.Repo.clone_from("https://github.com/zsh-users/zsh-autosuggestions",
                        "/home/$USER/.oh-my-zsh/doas/plugins/zsh-autosuggestions")
    print(replacetext("plugins=(git)",
          "plugins=(\ngit\nzsh-autosuggestions\nzsh-syntax-highlighting\n)", zsh_alias))
    print(replacetext('ZSH_THEME="robbyrussell"',
          'ZSH_THEME="agnoster"', zsh_alias))
    print(findtext('DEFAULT_USER="'+getpass.getuser()+'"\nprompt_context(){}'))
    # shell aliases
    print(
        findtext("if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi", zshrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases"),
         "wb").write(zsh_response.content)


# only for Arch linux because it uses different package manager than debian etc
def arch():
    subprocess.run(["clear"], check=True, text=True)
    pacman_config()
    check_for_aur_helper()
    arch_app_list = ["paru", "-Suy", "--needed"]
    for app in arch_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    for app in common_packages.split(" "):
        if app == "'" or app == "\\" or app == "":
            continue
        arch_app_list.append(app)
    subprocess.run(
        arch_app_list, check=True, text=True)
    input("Press Enter to continue...")
    subprocess.run(["clear"], check=True, text=True)


# Debian only
def debian():
    subprocess.run(["clear"], check=True, text=True)
    subprocess.run(["chmod", "+x", "./utils/debian_sources.sh"],
                   check=True, text=True)
    subprocess.run(["./utils/debian_sources.sh"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "update"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "--assume-yes", "-y",
                    "install", "\\", debian_packages, common_packages], check=True, text=True)
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "qq", "install",
                    "--assume-yes", "y", "./steam.deb"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
    # Install fastfetch
    fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")
    git.Repo.clone_from(
        "https://github.com/LinusDierheimer/fastfetch.git", fastfetchpath)
    pathlib2.Path(fastfetchpath, "build").mkdir(parents=True, exist_ok=True)
    subprocess.run(["cmake", ".."], cwd=pathlib2.Path(
        fastfetchpath, "build"), check=True, text=True)
    subprocess.run(["cmake", "--build", ".", "-j$(nproc)", "--target", "fastfetch",
                    "--target", "flashfetch"], cwd=pathlib2.Path(fastfetchpath, "build"), check=True, text=True)
    shutil.rmtree(fastfetchpath)
    subprocess.run(["sudo", "apt", "-qq", "update"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "upgrade"], check=True, text=True)
    subprocess.run(["sudo", "apt", "-qq", "autoremove"], check=True, text=True)
    subprocess.run(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"], check=True, text=True)
    noto_emoji_apple()
    # Install Mangohud
    if not is_tool("mangohud"):
        mangohud()
    # Arduino cli
    open(pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz"), "wb").write(requests.get(
        "https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz").content)
    subprocess.run(["sudo", "tar", "xf", "arduino-cli.tgz",
                    "-C", "/usr/local/bin", "arduino-cli"], check=True, text=True)
    pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz").unlink()


def flatpak():
    # Install Flatpak packages (universal)
    subprocess.run(["clear"], check=True, text=True)
    for app in flatpak_packages.split(" "):
        subprocess.run(["flatpak", "install", "flathub", app],
                       check=True, text=True)


def doas():
    subprocess.run(["xdg-open", "https://pastebin.com/EK6hud2S"],
                   check=True, text=True)
    input("modify /etc/doas.conf as sudo \nand put the text on the website into it \nand then press enter...")


def oreo_cursors():
    # Oreo Cursors
    while True:
        subprocess.run(["clear"], check=True, text=True)
        subprocess.run(
            ["lolcat"], input="Do you want to compile and install oreo cursor?", check=True, text=True)
        yesno = input("(y/N):")
        subprocess.run(["clear"], check=True, text=True)
        if yesno.lower() == "n":
            exit()
        elif yesno.lower() == "y":
            oreo_cursors()
            break
        else:
            print("Please answer yes or no!")


def main():
    if pathlib2.Path("/etc/arch-release").is_file():
        arch()
    elif pathlib2.Path("/etc/lsb-release").is_file() or pathlib2.Path("/etc/debian_version").is_file() or pathlib2.Path("/etc/linuxmint/info").is_file():
        debian()
    flatpak()
    doas()
    oh_my_zsh()
    oreo_cursors()


if __name__ == "__main__":
    main()
