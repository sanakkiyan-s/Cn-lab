import socket

s = socket.socket()
host = 'localhost'
port = 8082

s.bind((host, port))
s.listen(1)

print(host)
print("Waiting for any incoming connection ... ")

conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str("Enter the name of the file to be transmitted: "))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)

print("File has been transmitted successfully")
