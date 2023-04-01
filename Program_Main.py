#!/usr/bin/env python3
import program_commands
import program_common
import program_arch
import program_debian
import Installer
is_server_install_type = True
desktop_environment = ""
audio_environment = ""
linux_distro = Installer.system


def main():
    global is_server_install_type, desktop_environment, audio_environment, linux_distro
    program_commands.run_script_check()
    if linux_distro == "arch":
        program_arch.arch()
        is_server_install_type = program_commands.choice_server_desktop_apps()
        if not is_server_install_type:
            desktop_environment = program_commands.choice_desktop_environment()
            audio_environment = program_commands.choice_audio_environment()
    elif linux_distro == "debian":
        program_debian.debian()
    program_common.Main()
    program_commands.clear_screen()
    program_commands.lolcat_print("The script has been completed...\nGoodbye!")
    program_commands.press_enter_to_continue()


if __name__ == "__main__":
    main()
