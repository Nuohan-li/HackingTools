import socket 

target_host = "127.0.0.1"
target_port = 9998

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.connect((target_host, target_port))
client_socket.sendto(b"ABCDEFGHIJKLMNOPQRSTUVWXYZ", (target_host, target_port))
data, addr = client_socket.recvfrom(4096)

print(data.decode())
client_socket.close()