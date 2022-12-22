import subprocess
import pathlib2
import requests
from program_commands import *
import shutil
import git


zsh_URL = "https://pastebin.com/raw/t5rM9rxa"
zsh_response = requests.get(zsh_URL)
zshrc = pathlib2.Path(pathlib2.Path.home(), r"/.zshrc")
zsh_alias = pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases")

common_packages = open("./packages/common.txt", "r").read()
common_packages = common_packages.replace("\n", " ")


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


def oh_my_zsh():
    subprocess.run(
        ["sh", "-c", '"$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"'], check=True, text=True)
    git.Repo.clone_from("https://github.com/zsh-users/zsh-syntax-highlighting.git",
                        "/home/"+get_user()+"/.oh-my-zsh/doas/plugins/zsh-syntax-highlighting")
    git.Repo.clone_from("https://github.com/zsh-users/zsh-autosuggestions",
                        "/home/"+get_user()+"/.oh-my-zsh/doas/plugins/zsh-autosuggestions")
    print(replacetext("plugins=(git)",
          "plugins=(\ngit\nzsh-autosuggestions\nzsh-syntax-highlighting\n)", zsh_alias))
    print(replacetext('ZSH_THEME="robbyrussell"',
          'ZSH_THEME="agnoster"', zsh_alias))
    print(findtext('DEFAULT_USER="'+get_user()+'"\nprompt_context(){}'))
    # shell aliases
    print(
        findtext("if [ -f ~/.zsh_aliases ]; then\n. ~/.zsh_aliases\nfi", zshrc))
    open(pathlib2.Path(pathlib2.Path.home(), r"/.zsh_aliases"),
         "wb").write(zsh_response.content)


def install_oreo_cursors():
    git.Repo.clone_from("https://github.com/varlesh/oreo-cursors.git",
                        pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
    subprocess.run(["ruby", "generator/convert.rb"],
                   cwd=pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["make", "build"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    subprocess.run(["sudo", "make", "install"], cwd=pathlib2.Path(
        pathlib2.Path.cwd(), "oreo-cursors"), check=True, text=True)
    shutil.rmtree(pathlib2.Path(pathlib2.Path.cwd(), "oreo-cursors"))
