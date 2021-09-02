'''
since this is a client socket, we can create the server socket using Python
we can also create the server socket using netcat
'''
import socket

client_socket = socket.socket()

try:
    client_socket.connect(("0.0.0.0", 1339)) # make sure correct port is used
    client_socket.send("Hello There let me in".encode())
except:
    print("Connection refused")


# https://realpython.com/python-sockets/