import socket
client = socket.socket() 
# creating an instance of the socket 
client.connect((socket.gethostname(), 2000))  
# since we are running the clients and the pkda on the same system
# therefore we can use get gethostname for the ip address to
# connect to the server
client.send("Does the client communicate with pkda".encode())
client.close()