import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

message = 'Hello, world'
s.send(message.encode('utf-8'))

data = s.recv(1024)
s.close()

print('Received', data)
