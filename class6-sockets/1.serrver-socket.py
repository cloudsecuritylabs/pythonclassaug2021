'''
1. create a server socket using Python
2. connect to the server socket created using Python from nc
3. #nc localhost 50002
'''
import socket
new_socket = socket.socket()
# new_socket = socket.socket(socket.AF_INET, socket.d)
# IP -> string, port -> Integer
new_socket.bind(("0.0.0.0", 60002)) # this takes a Tuple!
new_socket.listen(4)
conn, addr = new_socket.accept() # this takes two variable
print(conn)
print(addr)
new_socket.close()



