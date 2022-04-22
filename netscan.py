import time
import scapy.all as scapy
import optparse
import requests
# allow user to get the MAC address of the desired device only or a IP prefix
parser = optparse.OptionParser()
parser.add_option('-t', dest='target', help='Enter the IP address of the target or an IP prefix')
(option, arg) = parser.parse_args()

# creating an ARP request that says "ARP who has 192.168.2.133, says 192.168.2.145"
arp_request = scapy.ARP()
# pdst field is the ARP target's IP address
# print(arp_request.show())
if option.target:
    arp_request.pdst = option.target
else:
    arp_request.pdst = '192.168.2.0/24'
# returns a list of options that can be set
# scapy.ls(scapy.ARP())

# set the destination MAC to broadcast MAC. scapy.Ether() returns 90:21:53:eb:be:78 > ff:ff:ff:ff:ff:ff (0x9000)
broadcast = scapy.Ether()
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

# create an ARP broadcast packet
arp_broadcast = broadcast/arp_request
#arp_broadcast.show()

# send the broadcast packet and captures the responses
answered_packets = scapy.srp(arp_broadcast, timeout=1)[0]
# response is Ether / ARP who has 192.168.2.133 says 192.168.2.145 ==> Ether / ARP is at 00:0c:29:99:e9:2d says 192.168.2.133 / Padding
print(answered_packets.show())
# getting the ARP response and getting the target IP address and MAC address, also display the result
print('---------------------------------------------------------------------------------------------')
print(' IP Address\t\t\tMAC Address\t\t\tVendor')
print('---------------------------------------------------------------------------------------------')
for element in answered_packets:
    # print(element)
    time.sleep(1)
    vendor = requests.get('http://api.macvendors.com/' + element[1].hwsrc).text
    print(' ' + element[1].psrc + '\t\t\t' + element[1].hwsrc + '\t\t' + vendor)
    print('---------------------------------------------------------------------------------------------')