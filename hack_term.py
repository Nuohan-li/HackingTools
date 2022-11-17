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
    cmd_list = cmd.split()
    arg_list = cmd_list[1:]
    # [0::2] -> starting from index 0, iterate through every other element
    opts = arg_list[0::2]
    args = arg_list[1::2]
    if cmd_list[0] == "portscanner":
        log_info("portscanner is selected")
        port = ''
        ip = ''
        range = ''
        for opt in opts:
            if opt == '-p':
                index = opts.index(opt)
                port = args[index]
                log_debug(port)
            elif opt == '-i':
                index = opts.index(opt)
                ip = args[index]
                log_debug(ip)
            elif opt == '-r':
                index = opts.index(opt)
                range = args[index]
                log_debug(range)
        
        if range == '':
            subprocess.call(['python', 'portscanner.py', '-p', str(port), '-i', str(ip)])
        else:
            subprocess.call(['python', 'portscanner.py', '-r', str(range), '-i', str(ip)])


