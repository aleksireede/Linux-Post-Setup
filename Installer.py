#!/usr/bin/env python3
import subprocess
import program_commands
import program_common
import program_arch
import program_debian


def main():
    program_commands.run_script_check()
    if program_commands.os_check() == "arch":
        program_arch.arch()
    elif profram_commands.os_check() == "debian":
        program_debian.debian()
    if program_commands.yes_no_check("Do you want to install oh my zsh?"):
        program_commands.clear_screen()
        program_common.oh_my_zsh()
        program_commands.clear_screen()
    if program_commands.yes_no_check("Do you want to compile install oreo cursors?"):
        program_commands.clear_screen()
        program_common.install_oreo_cursors()
        program_commands.clear_screen()
    if program_commands.yes_no_check("Do you want to install noto color emoji apple font?"):
        program_commands.clear_screen()
        program_common.noto_emoji_apple()
    program_commands.clear_screen()
    program_commands.text_lolcat("The script has been competed...\nGoodbye!")
    program_commands.press_enter_to_continue()


if __name__ == "__main__":
    main()
