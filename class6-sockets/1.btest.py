'''
1. demo how easy it is to create client/sever using nc
2. Create a listing service using nc
3. Connect to the listening serving using Python
'''
import socket
# nc -l -p 3333

socket_new = socket.socket()
socket_new.connect(("localhost", 3333))
socket_new.sendall("hello from python!".encode())
m=socket_new.recvmsg(1024)
print(m)
socket_new.close()