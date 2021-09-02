import socket
mysocket = socket.socket()
mysocket.bind(('0.0.0.0', 1434))
mysocket.listen(1)
c, addr = mysocket.accept()
data = c.recv(1024).decode()
print(data)
mysocket.close()

# nc localhost 1434