import socket
mysocket = socket.socket()

mysocket.connect(('localhost', 50002))
mysocket.send("hello,I’m the client".encode())

serverData = mysocket.recv(2048).decode() # data returned by server
print(serverData)
mysocket.close()
