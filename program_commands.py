import shutil
import subprocess
import pathlib2
import sys
import os
import pwd
import getpass

welcome_text = open("welcome_text.txt", "r").read()
input_yes = ("y", "yes", "k", "kyllä", "ye", "kyl", "kyll", "kylä")
input_no = ("n", "no", "e", "ei", "eii", "eiii")
input_desktop = ("d", "de", "desk", "desktop", "dekstop", "deskto", "des")
input_server = ("s", "se", "ser", "server", "serv", "srv", "serve")


def get_user():
    """Try to find the user who called sudo/pkexec."""
    try:
        return os.getlogin()
    except OSError:
        # failed in some ubuntu installations and in systemd services
        pass
    try:
        user = os.environ['USER']
    except KeyError:
        # possibly a systemd service. no sudo was used
        return getpass.getuser()
    if user == 'root':
        try:
            return os.environ['SUDO_USER']
        except KeyError:
            # no sudo was used
            pass
        try:
            pkexec_uid = int(os.environ['PKEXEC_UID'])
            return pwd.getpwuid(pkexec_uid).pw_name
        except KeyError:
            # no pkexec was used
            pass
    return user


def is_tool(name):    # check if program exists
    return shutil.which(name) is not None


def insert_text(text, file):
    data = file.read_text()
    if text in data:
        return "Text already inserted:"+text
    data = data+text
    file.write_text(data)
    return "Text written"


def replace_text(search_text, replace_text, file):
    data = file.read_text()
    if search_text not in data and replace_text not in data:
        insert_text(replace_text, file)
        return
    if replace_text in data and search_text not in data:
        return "Text already replaced"+replace_text
    data = data.replace(search_text, replace_text)
    file.write_text(data)
    return "Text replaced"


def press_enter_to_continue():
    input("Press the Enter key to continue...")


def os_check():
    if sys.platform != "linux":
        print("This is only for linux!\nThe program will now terminate!\nGoodbye!")
        press_enter_to_continue()
        exit(1)
    if pathlib2.Path("/etc/arch-release").is_file():
        return "arch"
    elif pathlib2.Path("/etc/lsb-release").is_file() or pathlib2.Path("/etc/debian_version").is_file() or pathlib2.Path("/etc/linuxmint/info").is_file():
        return "debian"


def clear_screen():
    subprocess.run(["clear"], check=True, text=True)


def lolcat_print(lolcat_text):
    subprocess.run(["lolcat"], input=lolcat_text, check=True, text=True)


def run_script_check():
    clear_screen()
    lolcat_print(welcome_text)
    yes_no_check("Do you wish to run the script?")


def yes_no_check(greeting_text):
    while True:
        clear_screen()
        lolcat_print(greeting_text)
        yes_no = input("(y/N):")
        if yes_no.lower() in input_yes:
            clear_screen()
            return True
        elif yes_no.lower() in input_no:
            clear_screen()
            return False
        else:
            print("Please answer yes or no!")
            press_enter_to_continue()

def is_server():
    while True:
        clear_screen()
        lolcat_print(
            "do you want to install only (server) or all (desktop) applications?")
        choice = input("(s/D):")
        if choice.lower() in input_server:
            clear_screen()
            return True
        elif choice.lower() in input_desktop:
            clear_screen()
            return False
        else:
            print("Please answer server or desktop!")
            press_enter_to_continue()
