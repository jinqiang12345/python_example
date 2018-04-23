import socket
import sys

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))
serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()
    print("connect address: %s" % str(addr))
    msg = 'welcom! ' + "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()