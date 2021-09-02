import socket
try:
     mysocket = socket.socket()
     mysocket.bind(('0.0.0.0', 1339))
     mysocket.listen(1)
     c, addr = mysocket.accept()
     buffer = 5
     data = ""

     while True:
          packet = c.recv(buffer)
          parsed = packet.decode()
          data += parsed

          if len(packet) < buffer :
               print(f'full data -> {data}')
               break
except:
     print("done")


