import shutil
import subprocess
import pathlib2
import sys
import os
import pwd
import getpass

input_yes = ("y", "yes", "k", "kyllä", "ye", "kyl", "kyll", "kylä")
input_no = ("n", "no", "e", "ei", "eii", "eiii")
input_desktop = ("d", "de", "desk", "desktop", "dekstop", "deskto", "des")
input_server = ("s", "se", "ser", "server", "serv", "srv", "serve")
input_gnome = ("gnome", "g", "gn", "gno", "gnom", "gmone", "gnoum", "gnomw")
input_kde = ("k", "kd", "kde", "ked", "kdd", "kded")
input_pipewire = ("pw", "pipewire")
input_pulseaudio = ("pa", "pulse", "pulseaudio")


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
        subprocess.run(["sudo", "touch", file], text=True, check=True)
        subprocess.run(["sudo", "chmod", "777", file], text=True, check=True)
    data = file.read_text()
    if len(args) == 1:
        if args[0] in data:
            clear_screen()
            return print(f"Already in file:{file} text:{args[0]}")
        data = data+args[0]
    elif len(args) == 2:
        if args[1] in data:
            clear_screen()
            return print(f"Already replaced{args[1]}")
        data = data.replace(args[0], args[1])
    else:
        clear_screen()
        return print("invalid number of arguments")
    try:
        file.write_text(data)
    except PermissionError:
        subprocess.run(["sudo", "chmod", "777", file], text=True, check=True)
        file.write_text(data)
        subprocess.run(["sudo", "chmod", "655", file], text=True, check=True)
    clear_screen()
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
    clear_screen()
    subprocess.run(["lolcat"], input=lolcat_text, check=True, text=True)


def check_true_false(message: str, choice: str, input_list_true: list, input_list_false: list):
    '''Displays a message and gives user a choice and returns true/false based on the choice'''
    while True:
        clear_screen()
        lolcat_print(message)
        choice = input(choice)
        if choice.lower() in input_list_true:
            clear_screen()
            return True
        elif choice.lower() in input_list_false:
            clear_screen()
            return False
        else:
            print("Please answer"+choice)
            press_enter_to_continue()


def choice_desktop_environment():
    if check_true_false("do you want to install gnome or kde desktop environment", "(g/K):", input_gnome, input_kde):
        return "gnome"
    else:
        return "kde"


def choice_server_desktop_apps():
    return check_true_false("do you want to install only (server) or all (desktop) applications?", "(s/D):", input_server, input_desktop)


def run_script_check():
    if check_true_false("Do you wish to run the script?", "(y/N):", input_yes, input_no):
        return
    else:
        exit(1)


def choice_audio_environment():
    if check_true_false("do you want to install pipewire or pulseaudio as audio backend", "(pw/PA):", input_pipewire, input_pulseaudio):
        return "pipewire"
    else:
        return "pulseaudio"
