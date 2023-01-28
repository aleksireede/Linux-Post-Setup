import subprocess
import pathlib2
import requests
import program_commands
import shutil
import git


zsh_URL = "https://pastebin.com/raw/t5rM9rxa"
zsh_response = requests.get(zsh_URL)
zshrc = pathlib2.Path("/home/", program_commands.get_user(), "/.zshrc")
zsh_alias = pathlib2.Path(
    "/home/", program_commands.get_user(), "/.zsh_aliases")

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
    if program_commands.is_server():
        return
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


def oh_my_zsh():
    subprocess.run(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended', shell=True)
    if pathlib2.Path("/home/", program_commands.get_user(), "/.oh-my-zsh/custom/plugins").exists():
        return
    git.Repo.clone_from("https://github.com/zsh-users/zsh-syntax-highlighting.git",
                        pathlib2.Path("/home/", program_commands.get_user(), "/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"))
    git.Repo.clone_from("https://github.com/zsh-users/zsh-autosuggestions",
                        pathlib2.Path("/home/", program_commands.get_user(), "/.oh-my-zsh/custom/plugins/zsh-autosuggestions"))
    print(program_commands.replace_text("plugins=(git)",
          "plugins=(\ngit\nzsh-autosuggestions\nzsh-syntax-highlighting\n)", zsh_alias))
    print(program_commands.replace_text('ZSH_THEME="robbyrussell"',
          'ZSH_THEME="agnoster"', zsh_alias))
    print(program_commands.insert_text('DEFAULT_USER="' +
          program_commands.get_user()+'"\nprompt_context(){}'))
    print(    # shell aliases
        program_commands.insert_text("if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi", zshrc))
    open(zsh_alias, "wb").write(zsh_response.content)


def install_oreo_cursors():
    if pathlib2.Path("/usr/share/icons/oreo_blue_cursors/cursor.theme").exists() or program_commands.is_server():
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
