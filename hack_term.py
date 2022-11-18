import subprocess
import os
import platform
import socket
import time
from misc import * 

path = '/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

def ping(host, count):
    param = '-n' if platform.system().lower == 'windows' else '-c'
    command = ['ping', param, count, host]
    return subprocess.call(command)

print("Hack Terminal")
while(True):
    cmd = input(">>> ")
    match cmd:
        case "portscanner":
            log_info("portscanner is selected")
            while(True):
                ip = input(">>> Enter target IP address: ")
                if ip == '':
                    log_error("You must provide an IP address")
                else:
                    break
                    

            protocol = input(">>> Enter the protocol the port is running, default is TCP: ")
            ports = input(">>> Enter the number of ports to scan: ")
            
            subprocess.call(['python', 'portscan.py', '-p', str(protocol), '-i', str(ip), '-r', str(ports)])

