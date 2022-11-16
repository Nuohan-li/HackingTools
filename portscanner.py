import socket
import sys
import getopt 
from misc import *

arg_port = ''
arg_host_ip = ''
arg_range = ''
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:i:", ["port=", "host_ip="])
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

log_info("Host IP and port specified is IP: {} Port: {}".format(arg_host_ip, arg_port))
# connect_ex: https://docs.python.org/3/library/socket.html
def port_scan(arg_port):
    if socket1.connect_ex((arg_host_ip,arg_port)):
        log_info("port {} is closed".format(arg_port))
    else:
        log_info("port {} is open".format(arg_port))



port_scan(arg_port)
