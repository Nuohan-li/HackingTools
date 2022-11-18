import socket
import sys
import getopt 
from misc import *
from threading import *

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
socket1.settimeout(10.0)

# host_ip = '192.168.1.29'
# port = 80

def port_scan(ip, port):
    try:
        socket1.connect((ip, int(port))) 
        log_notice("open port: " + str(port) + "   " + "service: " + socket.getservbyport(port, protocol))
        socket1.close()
    except socket.timeout:
        log_error("Timeout... Unable to connect to this address")
        quit()
    except Exception:
        pass

    # try:
    #     if socket1.connect_ex((ip,int(port))):
    #         # log_info("port {} is closed".format(port))
    #         pass 
    #     else:
    #         log_notice("port {} is open".format(port))
    # except:
    #     log_error("Time out")
    #     sys.exit(2)

if arg_range == '':
    log_info("Host IP and port specified is IP: {} Port: {}".format(arg_host_ip, arg_port))
    port_scan(arg_host_ip, arg_port)

else:
    log_info("Host IP and range specified is IP: {} Range: {}".format(arg_host_ip, arg_range))
    log_info("Scanning ports of range {}".format(arg_range))
    starting_index = int(arg_range.split('-')[0])
    end_index = int(arg_range.split('-')[1])
    for port in range(starting_index, end_index):
        port_scan(arg_host_ip, port)

# connect_ex: https://docs.python.org/3/library/socket.html



