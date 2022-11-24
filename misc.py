
from __future__ import print_function
from datetime import datetime
from termcolor import colored
import time
import sys

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def log_info(msg="", end='\n'):
    print('|' + now + '| INFO   : ' + colored(msg, 'green'), end=end)

def log_debug(msg="", end='\n'):
    print('|' + now + '| DEBUG  : ' + colored(msg, 'cyan'), end=end)

def log_warning(msg="", end='\n'):
    print('|' + now + '| WARNING: ' + colored(msg, 'yellow'), end=end)

def log_error(msg="", end='\n'):
    print('|' + now + '| ERROR  : ' + colored(msg, 'red'), end=end)

def log_notice(msg="", end='\n'):
    print('|' + now + '| NOTICE : ' + colored(msg, 'magenta'), end=end)

def progress(progress, total):
    percent = 100 * (progress / float(total))
    # bar = '#' * int(percent) + '_' * (100 - int(percent))
    # print(f"|{bar}|", end="\r") 
    # sys.stdout.flush()
    print(f"Current progress: {percent:.2f}%", end="\r")
    sys.stdout.flush()