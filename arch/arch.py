# Importing Path from pathlib2 module
from pathlib2 import Path
  
file = Path(r"/etc/pacman.conf")
# Creating a function to
# replace the text
def replacetext(search_text, replace_text, global file):
    # Reading and storing the content of the file in
    # a data variable
    data = file.read_text()
  
    # Replacing the text using the replace function
    data = data.replace(search_text, replace_text)
  
    # Writing the replaced data
    # in the text file
    file.write_text(data)
  
    # Return "Text replaced" string
    return "Text replaced"
  
# Calling the replacetext function
# and printing the returned statement
if file.exists():
    print(replacetext("#[multilib]", "[multilib]"))
    print(replacetext("#Include = /etc/pacman.d/mirrorlist", "Include = /etc/pacman.d/mirrorlist"))
    print(replacetext("#ParallelDownloads=5", "ParallelDownloads=5"))
    print(replacetext("#Color", "Color"))
