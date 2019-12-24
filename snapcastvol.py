import asyncio
import snapcast.control

loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, '192.168.0.241')) #snapcast server IP

# print all client names
for client in server.clients:
  print(client.friendly_name)
  print(client.identifier)
  print(client.group)

# set volume for client #0 to 50%

#client = server.clients[0]
client = 'b8:27:eb:b2:5f:83' #this is the client ID of the client you want to control
loop.run_until_complete(server.client_volume(client, {'percent': 10, 'muted': False}))
