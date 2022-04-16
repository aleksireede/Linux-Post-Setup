# Importing Path from pathlib2 module
from pathlib2 import Path

global file = Path(r"/etc/pulse/default.pa")
# Creating a function to
# replace the text
def replacetext(search_text, replace_text ,global file):
   
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
    print(replacetext("load-module module-bluetooth-policy", "load-module module-bluetooth-policy auto_switch=false"))
else:
    print("no pulseaudio file found. Are you sure you have pulseadio on your system?")
