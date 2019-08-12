#!/bin/bash
# script to use locally, to fade in after startup. use with "crontab -e" : "@reboot /home/volumio/volfadein.sh"
# don't forget to "sudo chmod +x volfadein.sh" 

x=5
while [ $x -le 100 ]
do
sleep 3s
echo "set value x to: $x"
/volumio/app/plugins/system_controller/volumio_command_line_client/volumio.sh volume +$x
x=$(( $x + 1 ))
done
