import socket
from rsa import *
from datetime import datetime
import json
import ast

def send_msg(client):
    nonce = 5
    request = {'id':'A','time':str(datetime.now()),'N1':nonce,"Duration":5,'Message':"This is the first message"}
    nonce+=1
    client.send(str(encrypt(json.dumps(request),public_key_B)).encode())

    data_recv = client.recv(1024).decode()
    data_recv = decrypt(ast.literal_eval(data_recv),private_key)
    data_recv = json.loads(data_recv)

    if data_recv['N1'] == nonce:
        print("Got first")
        request = {'id':'A','time':str(datetime.now()),'N1':nonce,"Duration":5,'Message':"This is the second message"}
        nonce+=1
        client.send(str(encrypt(json.dumps(request),public_key_B)).encode())

        data_recv = client.recv(1024).decode()
        data_recv = decrypt(ast.literal_eval(data_recv),private_key)
        data_recv = json.loads(data_recv)

        if data_recv['N1'] == nonce:
            print("Got second")
            request = {'id':'A','time':str(datetime.now()),'N1':nonce,"Duration":5,'Message':"This is the third message"}
            nonce+=1
            client.send(str(encrypt(json.dumps(request),public_key_B)).encode())

            data_recv = client.recv(1024).decode()
            data_recv = decrypt(ast.literal_eval(data_recv),private_key)
            data_recv = json.loads(data_recv)

            if data_recv['N1'] == nonce:
                print("Got third")

            else:
                print("Not Got Third")
        else:
            print("Not Got Second")
    else:
        print("Not Got It")

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


request = {'time':str(datetime.now()),'id':'B',"Duration":5}
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
public_key_B = data_recv['publicKey']
# the json we received
print(data_recv)
client.close()


client = socket.socket() 
# creating an instance of the socket 
client.connect((socket.gethostname(), 2001))  

request = {'id':'A','time':str(datetime.now()),'nonce':35,"Duration":5}
# I have made a nonce whose correct response should be n+1
request_to_send = json.dumps(request)

client.send(str(encrypt(json.dumps(request_to_send),public_key_B)).encode())

data_recv = client.recv(1024).decode()
data_recv = decrypt(ast.literal_eval(data_recv),private_key)
# print(data_recv)
data_recv = json.loads(data_recv)
if data_recv['N1']!= request['nonce']+1:
    print("Incorrect Nonce")
else:
    request = {'id':'A','time':str(datetime.now()),'N2':data_recv['N2']+1,"Duration":5}
    print("Data received "+str(data_recv))
    client.send(str(encrypt(json.dumps(request),public_key_B)).encode())
    send_msg(client)
client.close()
