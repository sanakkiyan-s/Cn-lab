import socket

UDP_IP = "localhost"
UDP_PORT = 8081

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

ip = ["172.16.1.9", "172.16.1.8"]
mac = ["6A:08:AA:C2", "8A:BC:E3:FA"]

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')
    if message:
        print("Received message:", message)
        break

for address in ip:
    if message in address:
        index = ip.index(message)
        print("The MAC address is:", mac[index])
