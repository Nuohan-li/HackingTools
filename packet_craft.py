from scapy.all import *
import subprocess
from uuid import getnode as get_mac
import re
from misc import *
import socket


def icmp_packet(**kwargs):

    host_name = socket.gethostname()
    # **kwargs returns key value pairs, need to check and set up default value manually
    ttl = 64
    src = socket.gethostbyname(host_name)
    dst = "192.168.1.87"
    data_size = 1000
    data = RandString(size=data_size)
    
    packet = IP()/ICMP()/Raw(data)
    packet.src = src
    packet.dst = dst
    packet.ttl = ttl
    packet.show2()
    return packet


def send_packet(packet, count=1):
    log_info("Sending {} ICMP packets".format(count))
    i = 0
    while i < count:
        print("source: " + packet.src + " destination: " + packet.dst + " sequence: " + str(packet.seq))
        packet.seq += 1
        send(packet)
        i += 1


def get_mac_addr():
    pass


send_packet(icmp_packet(data_size=80000, dst="192.168.1.30"), 10)
# icmp_packet()