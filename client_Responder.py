import socket
from rsa import *
from datetime import datetime
import json
# Responder
pkda_public_key = (209897, 163151)


# generating keys and commenting that part
# later if needed we can use it
# key = gen_keys(generate_primes(10),generate_primes(10))
# print(key)
# # ((1003643, 872779), (1003643, 117979))
# public_key = key[0]
# private_key = key[1]
public_key = (1003643, 872779)
private_key = (1003643, 117979)

client = socket.socket() 
# creating an instance of the socket 
client.connect((socket.gethostname(), 2000))  

# since we are running the clients and the pkda on the same system
# therefore we can use get gethostname for the ip address to
# connect to the server

client.send("Does the client communicate with pkda".encode())
client.close()
