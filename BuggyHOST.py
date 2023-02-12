import socket
import time


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
port = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip_address, port))
s.listen(3)
connection, addr = s.accept()
print("Connection established to " + addr[0])
data = connection.recv(256)
print(data.decode("utf-8"))
while True:
    cmd = input("Command: ")
    connection.send(bytes(cmd, "utf-8"))
    time.sleep(3)
    data = connection.recv(1024)
    print(data.decode("utf-8"))



connection.close()
