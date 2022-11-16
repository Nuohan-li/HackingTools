from scapy.all import *
import subprocess
from uuid import getnode as get_mac
import re

def icmp_packet(**kwargs):
    ttl = 64
    src = "10.0.2.15"
    dst = "192.168.1.29"
    data_size = 100
    
    packet = IP()/ICMP()/Raw(RandString(size=data_size))
    packet.src = src
    packet.dst = dst
    packet.ttl = ttl
    packet.show2()
    return packet


def send_packet(packet, count=1):
    send(packet, count=count)


def get_mac_addr():
    pass


send_packet(icmp_packet(data_size=8000), 10)
# icmp_packet()