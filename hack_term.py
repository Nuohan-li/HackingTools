import subprocess
import os
import platform
import socket
import time

path = '/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)

def ping(host, count):
    param = '-n' if platform.system().lower == 'windows' else '-c'
    command = ['ping', param, count, host]
    return subprocess.call(command)

print("Hack Terminal")
while(True):
    cmd = input(">>>")
    if cmd == "ping":
        host = input("enter website to ping")
        count = input("provide number of ping packets to send")
        print(ping(host, count))