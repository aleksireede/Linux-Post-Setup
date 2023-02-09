#!/usr/bin/env python3
import program_commands
import program_common
import program_arch
import program_debian
is_server=true


def main():
    is_server = program_commands.is_server()
    program_commands.run_script_check()
    if program_commands.os_check() == "arch":
        program_arch.arch()
    elif program_commands.os_check() == "debian":
        program_debian.debian()
    program_common.Main()
    program_commands.clear_screen()
    program_commands.lolcat_print("The script has been competed...\nGoodbye!")
    program_commands.press_enter_to_continue()


if __name__ == "__main__":
    main()
