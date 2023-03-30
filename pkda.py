# reference for socket program https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
import socket
server = socket.socket()
# creating a socket
server.bind((socket.gethostname(),2000))
# this is basically our master socket 
# binding that server to the host ip address and port 2000
server.listen(10)
# setting our public key distrbution authority such that it can listen to 10 clients
sock, conn_from = server.accept()

data_recv = sock.recv(1024).decode()
print("Data received "+str(data_recv))
sock.close()