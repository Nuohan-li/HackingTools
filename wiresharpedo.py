from scapy.all import *
import optparse
import socket 
from struct import *
from misc import *


sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

def format_mac(mac):
    """
    splitting the mac string into two parts, one of them starting from the beginning and get every other char
    the other part start from index 1 and also get every other char
    ex: 12345678 = 1357 and 2468
    then zip the two parts and iterate through them both at same time and concatenate them
    """
    mac_addr = ""
    mac1 = mac[::2]
    mac2 = mac[1::2]
    length = len(list(zip(mac1, mac2)))
    counter = 0
    for m1, m2 in zip(mac1, mac2):
        if counter < length - 1:
            mac_addr += m1+m2+":"
            counter += 1
        else:
            mac_addr += m1+m2
    return mac_addr


def write_to_pacp(pcap_path, packet):
    wrpcap(pcap_path, packet, append=True)



counter = 1
while 1:
    # receive packet from all 65535 ports
    packet = sock.recvfrom(65535)
    packet = packet[0]
    write_to_pacp("test1.pcap", packet)
    # print("packet is " + str(packet) + '\n')
    ether_length = 14
    ether_header = packet[:ether_length]
    # print(ether_header)
    # https://docs.python.org/3/library/struct.html -> unpack format
    # since dst and src MAC are 6 bytes = 6 s -> 6 bytes string, split into 2 char array of 6 bytes (MAC) and a unsigned short  
    ether = unpack('!6s6sH', ether_header)
    # print(ether)
    ether_type = hex(ether[2]).zfill(4)
    ether_type1 = "0x" + "{:04x}".format(ether[2])
    dst_MAC = ether[0].hex()
    src_MAC = ether[1].hex()
    print(f"packet {counter}: Destination MAC: {format_mac(dst_MAC)}, Source MAC: {format_mac(src_MAC)}, Ether type: {ether_type1}")
    counter += 1


# parser = optparse.OptionParser()
# parser.add_option('-i', dest='interface', help='enter the interface name where the packets will be sniffed')
# parser.add_option('-n', dest='file_name', help='name of the pcap file, default is packet.pcap')
# (options, arg) = parser.parse_args()

# if not options.interface:
#     print('please enter interface name')
#     quit()

# if not options.file_name:
#     print('please enter a file name')
#     quit()

# captured_packet = scapy.sniff(iface=options.interface)
# scapy.wrpcap(options.file_name, captured_packet)
