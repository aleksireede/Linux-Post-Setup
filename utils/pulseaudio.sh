#!/bin/bash
sudo sed -i "s/load-module module-bluetooth-policy/load-module module-bluetooth-policy auto_switch=false/" /etc/pulse/default.pa
#disable bluetooth hfp/hsp auto switch on ms teams
