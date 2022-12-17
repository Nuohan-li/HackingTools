import socket
import os 
import sys
import struct 
import binascii


def ether_header(data_received):
    ip_bool = False
    


socket_create = False
sniffer_socket = 0

if not socket_create:
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    socket_create = True

data_received = sniffer_socket.recv(2048)
os.system("clear")

data_received, ip_bool = ether_header(data_received)