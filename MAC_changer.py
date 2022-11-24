import subprocess
import optparse
import re
from misc import *

# to parse arguments
parser = optparse.OptionParser()

# dest is for accessing the argument later
parser.add_option('-i', dest="interface", help="name of interface whose MAC will be changed")
parser.add_option('-m', dest="MAC", help="new MAC address")

# args_parse captures every thing input by user and returns options and arguments, options.dest can be used to access the argument supplied by user
# parser.parse_arg() returns {'interface': 'eth0', 'MAC': '00:11:00:aa:cc:11'}
(options, arg) = parser.parse_args()

# if interface and options are empty
if not options.interface:
    parser.error('Please enter an interface')

# check if arguments are good
# return the output of the command, return bytes, need to be converted to string for search using regex
ifconfig = subprocess.check_output(["ifconfig", options.interface])

# search for the MAC address in ifconfig result & check if interface has MAC address
MAC_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig.decode('utf-8'))
if not MAC_search_result:
    log_error("This interface does not have MAC address")

if not options.MAC:
    log_error('Please enter a MAC address')

interface = options.interface
MAC = options.MAC

log_notice('Change MAC address of ' + interface + " to " + MAC)

# Python will run below commands; each element is a single word, prevents linux from reading ';'
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", MAC])
subprocess.call(["ifconfig", interface, "up"])

# get MAC after executing the command to check if the MAC is changed properly
current_ifconfig = subprocess.check_output(["ifconfig", options.interface])
current_MAC = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", current_ifconfig.decode('utf-8'))
if current_MAC.group(0).upper() == options.MAC.upper():
    log_info('MAC address has been changed')
else:
    log_error('Error, MAC could not be changed')
