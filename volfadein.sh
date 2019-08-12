#!/bin/bash
# script to fade in after reboot. use with crontab -e: @reboot volfadein.sh
# don't forget to "sudo chmod +x volfadein.sh" 

x=0
while [ $x -le 100 ]
do
sleep 3s
echo "set value x to: $x"
/volumio/app/plugins/system_controller/volumio_command_line_client/volumio.sh volume +$x
x=$(( $x + 1 ))
done
