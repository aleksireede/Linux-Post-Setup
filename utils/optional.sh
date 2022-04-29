#!/bin/bash

function utility(){
    while true; do
        read -p "$1 [Y/n]:" yn
        case $yn in
            [Yy]* ) $2; break;;
            [Nn]* ) break;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}
#loops through files with .sh ending and uses the below funtion "utility" to ask the user id they want to execute it
readarray -d '' files < <(find . -type f -name "*.sh" ! -name "optional*" ! -name "setup*" \
! -name "Packages*" ! -name "Installer*" ! -name "*.py" ! -name "*.conf" \
! -name "doas*" -print0)
for i in ${!files[@]}; do
  chmod u+x ${files[$i]}
  utility "Do you want to execute ${files[$i]}"  ${files[$i]}
done

