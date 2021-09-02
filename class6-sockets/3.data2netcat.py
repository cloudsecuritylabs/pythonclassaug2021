import socket
mysocket = socket.socket()
mysocket.connect(('localhost', 1334))
mysocket.send("hello,I’m the client".encode())
mysocket.close()