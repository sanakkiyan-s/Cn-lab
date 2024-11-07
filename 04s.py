import socket
import wmi

UDP_IP = "localhost"
UDP_PORT = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    str_data = data.decode("utf-8")
    print("Received message:", str_data)
    print("Opening", str_data)
    conn = wmi.WMI()
    pid, returnval = conn.Win32_Process.Create(CommandLine=str_data)
