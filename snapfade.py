import asyncio
import snapcast.control
from time import sleep      # Importing the time library to provide the delays in program
import os
os.system('sudo systemctl restart snapserver')

loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, 'localhost')) #snapcast server IP

# print all client names
#for client in server.clients:
#  print(client.friendly_name)
#  print(client.identifier)
#  print(client.group)



#client = server.clients[0] # set volume for client #0 to 50%
client = 'b8:27:eb:b2:5f:83' #this is the client ID of the client you want to control
loop.run_until_complete(server.client_volume(client, {'percent': 1, 'muted': False}))
os.system('/volumio/app/plugins/system_controller/volumio_command_line_client/volumio.sh next')

for i in range(2, 25):
   #print(i)
   sleep (5)
   loop.run_until_complete(server.client_volume(client, {'percent': i, 'muted': False}))
