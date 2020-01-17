#!/bin/bash
# script to use locally, to autostart+fade in after startup. use with "crontab -e" : "@reboot /home/volumio/volfadein.sh"
# don't forget to "sudo chmod +x volfadein.sh" 
sleep 38s
/volumio/app/plugins/system_controller/volumio_command_line_client/volumio.sh next
sudo systemctl restart snapserver
x=20 # start with volume 20
while [ $x -le 100 ]
do
sleep 3.5s # time to wait between increments
echo "set value x to: $x"
/volumio/app/plugins/system_controller/volumio_command_line_client/volumio.sh volume +$x
x=$(( $x + 2 )) # increment by 2
done
