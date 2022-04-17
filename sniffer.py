import scapy.all as scapy
import optparse

parser = optparse.OptionParser()
parser.add_option('-i', dest='interface', help='enter the interface name where the packets will be sniffed')
parser.add_option('-n', dest='file_name', help='name of the pcap file, default is packet.pcap')
(options, arg) = parser.parse_args()

if not options.interface:
    print('please enter interface name')
    quit()

if not options.file_name:
    print('please enter a file name')
    quit()

captured_packet = scapy.sniff(iface=options.interface)
scapy.wrpcap(options.file_name, captured_packet)
