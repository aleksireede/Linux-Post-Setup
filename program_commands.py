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


def text_modify(file, *args):
    file = pathlib2.Path(file)
    if not file.exists():
        f = open(file, "w")
    data = file.read_text()
    if len(args) == 1:
        if args[0] in data:
            return print(f"Already in file:{file} text:{args[0]}")
        data = data+args[0]
    elif len(args) == 2:
        if args[1] in data:
            return print(f"Already replaced{args[1]}")
        data = data.replace(args[0], args[1])
    else:
        return print("invalid number of arguments")
    file.write_text(data)
    return print(f"operation successfull args:{args}")


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
