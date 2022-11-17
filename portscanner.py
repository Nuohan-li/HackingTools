import socket
import sys
import getopt 
from misc import *

arg_port = ''
arg_host_ip = ''
arg_range = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:i:r:", ["port=", "host_ip="])
except:
    log_error("please provide a port number and IP address")
    sys.exit(2)

for opt,arg in opts:
    if opt in ("-p, --port"):
        arg_port = int(arg)
    elif opt in ("-i", "--ip"):
        arg_host_ip = arg.replace(" ", "")
    elif opt in ("-r", "--range"):
        arg_range = arg


socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_ip = '192.168.1.29'
# port = 80

def port_scan(ip, port):
    socket1.settimeout(10)
    if socket1.connect_ex((ip,int(port))):
        log_info("port {} is closed".format(port))
    else:
        log_info("port {} is open".format(port))

if arg_range == '':
    log_info("Host IP and port specified is IP: {} Port: {}".format(arg_host_ip, arg_port))
else:
    log_info("Host IP and range specified is IP: {} Range: {}".format(arg_host_ip, arg_range))
    log_info("Scanning ports of range {}".format(arg_range))
    starting_index = int(arg_range.split('-')[0])
    print(starting_index)
    end_index = int(arg_range.split('-')[1])
    while starting_index != end_index:
        print(starting_index)
        port_scan(arg_host_ip, starting_index)
        starting_index += 1 
# connect_ex: https://docs.python.org/3/library/socket.html


port_scan(arg_host_ip, arg_port)

