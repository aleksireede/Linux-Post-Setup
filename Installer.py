#!/usr/bin/env python3
import subprocess
import pathlib2
import shutil
import requests
import git

bash_URL = "https://pastebin.com/raw/7B7hmX2a"
zsh_URL = "https://pastebin.com/raw/t5rM9rxa"
bash_response = requests.get(bash_URL)
zsh_response = requests.get(zsh_URL)
bashrc = pathlib2.Path(pathlib2.Path.home(), r"/.bashrc")
zshrc = pathlib2.Path(pathlib2.Path.home(), r"/.zshrc")
welcome_text = open("welcome_text.txt", "r").read()
arch_packages = open("./packages/arch.txt", "r").read()
common_packages = open("./packages/common.txt", "r").read()
debian_packages = open("./packages/debian.txt", "r").read()
flatpak_packages = open("./packages/flatpak.txt", "r").read()
arch_packages = arch_packages.replace("\n", " ")
common_packages = common_packages.replace("\n", " ")
doas_path = pathlib2.Path(pathlib2.Path.cwd(), "doas")
doas_conf_path = pathlib2.Path(r"/usr/local/etc/doas.conf")
pacman_conf = pathlib2.Path(r"/etc/pacman.conf")

while True:
    subprocess.call(["clear"])
    subprocess.run(["lolcat"], input=welcome_text, text=True)
    subprocess.run(
        ["lolcat"], input="Do you wish to run the script?", text=True)
    yes_no = input("(y/N):")
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
    subprocess.call(["ruby", "generator/convert.rb"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["make", "build"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["sudo", "make", "install"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.call(["clear"])


def asus_linux():
    git.Repo.clone_from("https://gitlab.com/asus-linux/asusctl.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["make"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["sudo", "make", "install"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "asusctl"))
    subprocess.call(["clear"])


def check_for_aur_helper():
    if is_tool("paru") or is_tool("yay"):
        return
    subprocess.call(["sudo", "pacman", "-S", "--needed", "base-devel"])
    subprocess.call(
        ["git", "clone", "https://aur.archlinux.org/paru.git"])
    subprocess.call(["makepkg", "-si"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "paru"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "paru"),
                  ignore_errors=False, onerror=None)


def arch_doas():
    if is_tool("doas"):
        return
    git.Repo.clone_from("https://aur.archlinux.org/doas.git", doas_path)
    subprocess.call(["makepkg", "-si"], cwd=doas_path)
    doas_part_two()
    doas_part_three()


def debian_doas():
    if is_tool("doas"):
        return
    git.Repo.clone_from("https://github.com/slicer69/doas.git",
                        doas_path)
    subprocess.run(["make"],
                    cwd=doas_path,shell=True)
    subprocess.run(["sudo", "make", "install"],
                    cwd=doas_path,shell=True)
    doas_part_two()
    doas_part_three()


def doas_part_two():
    if doas_conf_path.exists():
        return
    subprocess.run(["sudo", "chmod", "777", doas_conf_path],shell=True)
    open(doas_conf_path, "wb"
         ).write(requests.get("https://pastebin.com/raw/EK6hud2S").content)
    subprocess.run(["sudo", "dos2unix", doas_conf_path],shell=True)
    subprocess.run(["sudo", "chmod", "644", doas_conf_path],shell=True)
    subprocess.run(["sudo", "chown", "root:root", doas_conf_path],shell=True)


def doas_part_three():
    shutil.rmtree(doas_path)
    subprocess.run(["doas", "chmod", "777", "/usr/bin/sudo"],shell=True)
    shutil.rmtree(pathlib2.Path("/usr/bin/sudo"))
    pathlib2.Path(
        '/usr/bin/sudo').symlink_to(pathlib2.Path('/usr/bin/doas'))


def pacman_config():
    if not pacman_conf.exists():
        return
    subprocess.run(["sudo", "chmod", "777", pacman_conf])
    print(replacetext("#[multilib]\n#Include = /etc/pacman.d/mirrorlist",
          "[multilib]\nInclude = /etc/pacman.d/mirrorlist", pacman_conf))
    print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5", pacman_conf))
    print(replacetext("#Color", "Color", pacman_conf))
    print(findtext(
        "[g14]\nSigLevel = DatabaseNever Optional TrustAll\nServer = https://arch.asus-linux.org", pacman_conf))
    subprocess.call(["sudo", "chmod", "644", pacman_conf])


def mangohud():
    git.Repo.clone_from("https://github.com/flightlessmango/MangoHud.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.call(["chmod", "+x", "./build.sh"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.call(["./build.sh", "build"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.call(["./build.sh", "install"],
                    cwd=pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "Mangohud"))
    subprocess.call(["clear"])


# only for Arch linux because it uses different package manager than debian etc
if pathlib2.Path("/etc/arch-release").is_file():
    subprocess.call(["clear"])
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
    subprocess.run(arch_app_list, shell=True, text=True)
    subprocess.call(["clear"])
    arch_doas()
    subprocess.call(["sudo", "systemctl", "enable", "--now",
                    "power-profiles-daemon.service"])
    subprocess.call(["sudo", "systemctl", "enable", "--now supergfxd"])


# Debian only
elif pathlib2.Path("/etc/lsb-release").is_file() or pathlib2.Path("/etc/debian_version").is_file() or pathlib2.Path("/etc/linuxmint/info").is_file():
    subprocess.call(["clear"])
    subprocess.run(["chmod", "+x", "./utils/debian_sources.sh"],shell=True)
    subprocess.run(["./utils/debian_sources.sh"],shell=True)
    subprocess.run(["sudo", "apt", "-qq", "update"],shell=True)
    subprocess.run(["sudo", "apt", "-qq", "--assume-yes", "-y",
                    "install", "\\", debian_packages, common_packages],shell=True)
    open(pathlib2.Path(pathlib2.Path.cwd(), "steam.deb"), "wb").write(requests.get(
        "https://cdn.akamai.steamstatic.com/client/installer/steam.deb").content)
    subprocess.run(["sudo", "apt", "qq", "install",
                    "--assume-yes", "y", "./steam.deb"],shell=True)
    pathlib2.Path(pathlib2.Path.cwd(), "steam.deb").unlink()
    # Install fastfetch
    fastfetchpath = pathlib2.Path(pathlib2.Path.cwd(), "fastfetch")
    git.Repo.clone_from(
        "https://github.com/LinusDierheimer/fastfetch.git", fastfetchpath)
    pathlib2.Path(fastfetchpath, "build").mkdir(parents=True, exist_ok=True)
    subprocess.run(["cmake", ".."], cwd=pathlib2.Path(fastfetchpath, "build"))
    subprocess.run(["cmake", "--build", ".", "-j$(nproc)", "--target", "fastfetch",
                    "--target", "flashfetch"], cwd=pathlib2.Path(fastfetchpath, "build"))
    shutil.rmtree(fastfetchpath)
    subprocess.run(["sudo", "apt", "-qq", "update"],shell=True)
    subprocess.run(["sudo", "apt", "-qq", "upgrade"],shell=True)
    subprocess.run(["sudo", "apt", "-qq", "autoremove"],shell=True)
    subprocess.run(
        ["xdg-open", "https://discord.com/api/download?platform=linux&format=deb"],shell=True)
    debian_doas()
    # Install asus-linux
    while True:
        subprocess.call(["clear"])
        subprocess.call(
            ["lolcat"], input="Do you want to compile and install asus-linux? (y/N):", text=True)
        yesno = input()
        if yesno.lower() == "n":
            exit()
        elif yesno.lower() == "y":
            asus_linux()
            break
        else:
            print("Please answer yes or no!")

# Install Flatpak packages (universal)
subprocess.call(["clear"])
for app in flatpak_packages.split(" "):
    subprocess.call(["flatpak", "install", "flathub", app])

# shell aliases
if bashrc.exists():
    print(
        findtext("if [ -f ~/.bash_aliases ]; then\n. ~/.bash_aliases\nfi", bashrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.bash_aliases"),
         "wb").write(bash_response.content)
elif zshrc.exists():
    print(
        findtext("if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi", zshrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases"),
         "wb").write(zsh_response.content)

# Make nemo default file manager
subprocess.call(["xdg-mime", "default", "nemo.desktop",
                "inode/directory", "application/x-gnome-saved-search"])

# Arduino cli
open(pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz"), "wb").write(requests.get(
    "https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz").content)
subprocess.call(["sudo", "tar", "xf", "arduino-cli.tgz",
                "-C", "/usr/local/bin", "arduino-cli"])
pathlib2.Path(pathlib2.Path.cwd(), "arduino-cli.tgz").unlink()

# Notocolor emoji apple
open(pathlib2.Path(r"/tmp/NotoColorEmoji.ttf"), "wb").write(requests.get(
    "https://gitlab.com/timescam/noto-fonts-emoji-apple/-/raw/master/NotoColorEmoji.ttf?inline=false").content)
if pathlib2.Path(r"/usr/share/fonts/truetype/").exists():
    if pathlib2.Path(r"/usr/share/fonts/truetype/NotoColorEmoji.ttf").exists():
        subprocess.call(
            ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"])
    subprocess.call(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                     "/usr/share/fonts/truetype/NotoColorEmoji.ttf"])
elif pathlib2.Path(r"/usr/share/fonts/noto/").exists():
    if pathlib2.Path(r"/usr/share/fonts/noto/NotoColorEmoji.ttf").exists():
        subprocess.call(
            ["sudo", "rm", "/usr/share/fonts/truetype/NotoColorEmoji.ttf"])
    subprocess.call(["sudo", "mv", "/tmp/NotoColorEmoji.ttf",
                     "/usr/share/fonts/noto/NotoColorEmoji.ttf"])
subprocess.call(["clear"])

# Install Mangohud
if not is_tool("mangohud"):
    mangohud()


# Oreo Cursors
while True:
    subprocess.call(["clear"])
    subprocess.run(
        ["lolcat"], input="Do you want to compile and install oreo cursor?", text=True)
    yesno = input("(y/N):")
    subprocess.call(["clear"])
    if yesno.lower() == "n":
        exit()
    elif yesno.lower() == "y":
        oreo_cursors()
        break
    else:
        print("Please answer yes or no!")
