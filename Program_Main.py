#!/usr/bin/env python3
import program_commands
import program_common
import program_arch
import program_debian
is_server_apps = True
desktop_environment = "gnome"
audio_environment = "pipewire"
linux_distro = ""


def main():
    global is_server_apps, desktop_environment, audio_environment, linux_distro
    program_commands.run_script_check()
    is_server_apps = program_commands.choice_server_desktop_apps()
    desktop_environment = program_commands.choice_desktop_environment()
    audio_environment = program_commands.choice_audio_environment()
    if program_commands.os_check() == "arch":
        linux_distro = "arch"
        program_arch.arch()
    elif program_commands.os_check() == "debian":
        linux_distro = "debian"
        program_debian.debian()
    program_common.Main()
    program_commands.clear_screen()
    program_commands.lolcat_print("The script has been completed...\nGoodbye!")
    program_commands.press_enter_to_continue()


if __name__ == "__main__":
    main()
