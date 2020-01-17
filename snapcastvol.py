import asyncio
import snapcast.control
from time import sleep      # Importing the time library to provide the delays in program
sleep (35)
loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, 'localhost')) #snapcast server IP

# print all client names. do this first to find out client IDs. you can also do this with the android app snapcontrol or by just finding out the mac address of the client

#for client in server.clients:
#  print(client.friendly_name)
#  print(client.identifier)
#  print(client.group)


client = 'b8:27:eb:b2:5f:83' #this is the client ID of the client you want to control
loop.run_until_complete(server.client_volume(client, {'percent': 2, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 4, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 6, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 8, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 10, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 12, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 14, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 16, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 18, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 20, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 22, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 24, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 26, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 28, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 30, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 32, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 34, 'muted': False}))
sleep (4)
loop.run_until_complete(server.client_volume(client, {'percent': 36, 'muted': False}))
