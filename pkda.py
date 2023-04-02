# reference for socket program https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
import socket
from rsa import *
from datetime import datetime
import json
# Pkda

def req_handler(data_recv,sock):
    request_recv = json.loads(data_recv)
    request_recv['publicKey'] = keys_dict[request_recv['id']]
    request_recv['nonce']+=1
    response = encrypt(json.dumps(request_recv),private_key)
    sock.send(str(response).encode())
    

# generating keys and commenting that part
# later if needed we can use it
# key = gen_keys(generate_primes(10),generate_primes(10))
# print(key)
# ((209897, 163151), (209897, 34811))
# public_key = key[0]
# private_key = key[1]
#
public_key = (209897, 163151)
private_key = (209897, 34811)
keys_dict = {'B':'(1003643, 872779)','A':'(625967, 105343)'}

server = socket.socket()
# creating a socket
server.bind((socket.gethostname(),2000))
# this is basically our master socket 
# binding that server to the host ip address and port 2000
server.listen(10)
# setting our public key distrbution authority such that it can listen to 10 clients

# initiator 
sock, conn_from = server.accept()
data_recv = sock.recv(1024).decode()
print("Data received "+str(data_recv))
req_handler(data_recv,sock)

# responder
sock, conn_from = server.accept()
data_recv = sock.recv(1024).decode()
print("Data received "+str(data_recv))
req_handler(data_recv,sock)
sock.close()

