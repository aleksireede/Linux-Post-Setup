#!/usr/bin/env python3
import subprocess
from program_commands import *
from program_debian import *
from program_arch import *
from program_common import *


def main():
    run_script_check()
    if os_check() == "arch":
        arch()
    elif os_check() == "debian":
        debian()
    if yes_no_check("Do you want to install oh my zsh?"):
        clear_screen()
        oh_my_zsh()
        clear_screen()
    if yes_no_check("Do you want to compile install oreo cursors?"):
        clear_screen()
        install_oreo_cursors()
        clear_screen()
    if yes_no_check("Do you want to install noto color emoji apple font?"):
        clear_screen()
        noto_emoji_apple()
    clear_screen()
    lolcat_text("The script has been competed...\nGoodbye!")
    press_enter_to_continue()


if __name__ == "__main__":
    main()
