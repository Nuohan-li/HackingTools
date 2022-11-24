from scapy.all import *
import subprocess
from uuid import getnode as get_mac
import re
from misc import *
import socket


def icmp_packet(**kwargs):

    host_name = socket.gethostname()
    # **kwargs returns key value pairs, need to check and set up default value manually
    ttl = kwargs.get("ttl", 64)
    src = socket.gethostbyname(host_name)
    dst = kwargs.get("dst", "192.168.1.87")
    data_size = kwargs.get("data_size", 1000)
    data = RandString(size=data_size)
    
    packet = IP()/ICMP()/Raw(data)
    packet.src = src
    packet.dst = dst
    packet.ttl = ttl
    packet.show2()
    return packet


def arp_packet(**kwargs):
    
    packet = Ether()
    packet.hwdst = kwargs.get("dst", "ff:ff:ff:ff:ff:ff")
    packet.hwsrc = kwargs.get("src", "08:00:27:22:46:4f")
    packet.type = 0x806

    arp_content = ARP()
    arp_content.pdst = kwargs.get("pdst", "10.0.0.1")
    arp_content.psrc = kwargs.get("psrc", "10.0.0.184")
    arp_content.op = kwargs.get("op", 1)

    packet = packet/arp_content
    # packet.show2()
    return packet
    # answer = send(packet)
    # print(answer)
    # print(answer[0].show())
    # answer[0][0][1].show()


def syn_flood_packet(**kwargs):
    IPlayer = IP()
    IPlayer.src = kwargs.get("src", socket.gethostbyname(socket.gethostname()))
    IPlayer.dst = kwargs.get("dst")

    TCPlayer = TCP()
    TCPlayer.dport = kwargs.get("dport")
    # TCPlayer.sport = kwargs.get("sport")
    
    rawlayer = Raw()
    rawlayer.load = RandString(size = kwargs.get("size"))
    packet = IPlayer/TCPlayer/rawlayer
    return packet


def send_packet(packet, count=1):
    log_info("Sending {} ICMP packets".format(count))
    i = 0
    while i < count:
        print("source: " + packet.src + " destination: " + packet.dst + " sequence: " + str(packet.seq))
        packet.seq += 1
        send(packet)
        i += 1



arp_packet()
# icmp_packet(data_size=10000, dst="192.168.1.30")
# send_packet(icmp_packet(data_size=80000, dst="192.168.1.30"), 10)
# icmp_packet()