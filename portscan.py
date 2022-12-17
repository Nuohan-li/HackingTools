import optparse
import socket
from misc import *

# add options 
parser = optparse.OptionParser()
parser.add_option('-i', dest='target_ip', help="enter the target device's IP address")
parser.add_option('-p', dest='protocol', help="enter the protocol you are scanning for, default = tcp")
parser.add_option('-r', dest='ports', help="enter how many ports do you want to scan, default = 65535")
(options, arg) = parser.parse_args()

ports = 1
protocol = ""

# force user to enter an IP address
if not options.target_ip:
    print("please provide target's IP address")
    quit()

if not options.ports:
    ports = 65535
else:
    ports = int(options.ports)

if not options.protocol:
    protocol = "tcp"
else:
    protocol = options.protocol

# creating a socket and try to connect to every single port of the target to determine which port on target machine is
# open, and what service is running on that port

for port in range(1, ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    progress(port, ports)
    try:
        sock.connect((options.target_ip, port)) 
        try:
            banner = sock.recv(4096).decode().strip('\n')
        except socket.timeout:
            continue
        # print("info" + info)
        print("open port: " + str(port) + "   " + "service: " + socket.getservbyport(port, protocol) + " banner: " + banner )
        sock.close()
    except socket.timeout:
        print("Timeout... Unable to connect to this address")
        quit()
    except Exception:
        pass

print(f"Complete. {ports} ports scanned")

