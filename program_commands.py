import shutil
import subprocess
import pathlib2
import re
import os
import pwd
import getpass
import platform

input_yes = ("y", "yes", "k", "kyllä", "ye", "kyl", "kyll", "kylä")
input_no = ("n", "no", "e", "ei", "eii", "eiii")
input_desktop = ("d", "de", "desk", "desktop", "dekstop", "deskto", "des")
input_server = ("s", "se", "ser", "server", "serv", "srv", "serve")
input_gnome = ("gnome", "g", "gn", "gno", "gnom", "gmone", "gnoum", "gnomw")
input_kde = ("k", "kd", "kde", "ked", "kdd", "kded")
input_pipewire = ("pw", "pipewire")
input_pulseaudio = ("pa", "pulse", "pulseaudio")
character_blacklist = "[^a-zA-Z0-9-_\n .+]"


def get_username():
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
        print("Username Auto-detect Failed!")
        user = input("Please enter your username:")
    return user


username = get_username()


def is_tool(name):
    return shutil.which(name) is not None


def text_modify(file, *args):
    file = pathlib2.Path(file)
    if not file.exists():
        try:
            subprocess.run(["sudo", "touch", file], text=True,
                           check=True, input=getpass.getpass())
            subprocess.run(["sudo", "chmod", "644", file],
                           text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(e)
            return

    data = file.read_text()
    if len(args) == 1:
        data = args[0]
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
        try:
            subprocess.run(["sudo", "chmod", "777", file],
                           text=True, check=True, input=getpass.getpass())
            file.write_text(data)
            subprocess.run(["sudo", "chmod", "644", file],
                           text=True, check=True)
        except subprocess.CalledProcessError as e:
            print(e)
            return

    clear_screen()
    return print(f"operation successful args:{args}")


def press_enter_to_continue():
    input("Press the Enter key to continue...")


def os_check():
    if pathlib2.Path("/etc/arch-release").is_file():
        return "arch"
    elif pathlib2.Path("/etc/lsb-release").is_file() or pathlib2.Path("/etc/debian_version").is_file() or pathlib2.Path("/etc/linuxmint/info").is_file():
        return "debian"
    if is_tool("termux-setup-storage"):
        return "android"

linux_distro = os_check()


def clear_screen():
    subprocess.run(["clear"], check=True, text=True)


def lolcat_print(lolcat_text):
    clear_screen()
    try:
        subprocess.run(["lolcat"], input=lolcat_text, check=True, text=True)
    except (subprocess.CalledProcessError,FileNotFoundError) as error:
        print(lolcat_text)


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


def choice_audio_environment():
    if check_true_false("do you want to install pipewire or pulseaudio as audio backend", "(pw/PA):", input_pipewire, input_pulseaudio):
        return "pipewire"
    else:
        return "pulseaudio"


def text_filter(text):
    return re.sub(character_blacklist, "", text).split("\n")


def detect_graphics_card():
    output = subprocess.check_output(['lspci', '-nnk']).decode('utf-8')
    if 'VGA compatible controller' in output:
        if 'NVIDIA Corporation' in output:
            print("Nvidia graphics card detected")
        elif 'Advanced Micro Devices, Inc.' in output:
            print("AMD graphics card detected")
        else:
            print("Unknown graphics card detected")
    else:
        print("No graphics card detected")


def check_machine_type():
    machine_type = platform.machine()
    if machine_type.startswith('arm') or machine_type.startswith("aarch64"):
        return "Arm"
    elif machine_type.startswith('x86'):
        return "x86"
    else:
        print('Unknown machine type')

cpu_architecture = check_machine_type()
