#!/bin/bash
if [ -f /etc/pulse/default.pa ]
then
sudo sed -i "s/load-module module-bluetooth-policy/load-module module-bluetooth-policy auto_switch=false/" /etc/pulse/default.pa
fi
#disable bluetooth hfp/hsp auto switch on ms teams
