#!/usr/bin/env python
import netfilterqueue
import os
import scapy.all as scapy

def process(pkt):
    # convert pkt to scapy packet
    
    scapy_pkt = scapy.IP(pkt.get_payload())
    print(scapy_pkt.show())

    pkt.accept()
    


try:
    # os.system("iptables -I FORWARD -j NFQUEUE --queue-num 0")
    os.system("iptables -I INPUT -j NFQUEUE --queue-num 0")
    os.system("iptables -I OUTPUT -j NFQUEUE --queue-num 0")
    nfqueue = netfilterqueue.NetfilterQueue()
    nfqueue.bind(0, process)
    nfqueue.run()
except KeyboardInterrupt:
    os.system("iptables --flush")