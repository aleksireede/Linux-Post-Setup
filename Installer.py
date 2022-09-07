#!/usr/bin/env python3
import subprocess
welcome_text = open("welcome_text.txt", "r").read()
welcome_print = subprocess.run(["lolcat"], input=welcome_text, text=True, )
welcome_print
while True:
    yes_no = input("Do you wish to run the script? [Y/n]:")
    if yes_no.lower() == "y" or yes_no.lower() == "yes":
        break
    elif yes_no.lower() == "n" or yes_no.lower() == "no":
        exit(1)
    else:
        print("Please answer yes or no!")
subprocess.run(["python3", "-m", "pip", "install",
               "pathlib2", "websockets", "yt-dlp"], text=True)
