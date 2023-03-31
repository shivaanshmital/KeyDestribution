import socket
from rsa import *
from datetime import datetime
import json
import ast

# Initiator
pkda_public_key = (209897, 163151)


# generating keys and commenting that part
# later if needed we can use it
# key = gen_keys(generate_primes(10),generate_primes(10))
# print(key)
# ((625967, 105343), (625967, 472447))
# public_key = key[0]
# private_key = key[1].

public_key = (625967, 105343)
private_key = (625967, 472447)


request = {'time':str(datetime.now()),'id':'B'}
request = json.dumps(request)



client = socket.socket() 
# creating an instance of the socket 
client.connect((socket.gethostname(), 2000))  

# since we are running the clients and the pkda on the same system
# therefore we can use get gethostname for the ip address to
# connect to the server

# client.send("Does the client communicate with pkda".encode())
client.send(request.encode())
data_recv = client.recv(1024).decode()
data_recv = decrypt(ast.literal_eval(data_recv),pkda_public_key)
# print("Data received "+str(data_recv))
data_recv = json.loads(data_recv)
data_recv['publicKey'] = eval(data_recv['publicKey'])
# the json we received
print(data_recv)
client.close()
