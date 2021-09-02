import socket
mysocket = socket.socket()
mysocket.bind(('0.0.0.0', 1334))
mysocket.listen(1)
print("waiting for connection...")
c, addr = mysocket.accept()
print("client that connected details are -> {}".format(addr))