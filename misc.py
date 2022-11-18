from datetime import datetime
from termcolor import colored

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def log_info(msg=""):
    print('|' + now + '| INFO: ' + colored(msg, 'green'))

def log_debug(msg=""):
    print('|' + now + '| DEBUG: ' + colored(msg, 'cyan'))

def log_warning(msg=""):
    print('|' + now + '| WARNING: ' + colored(msg, 'yellow'))

def log_error(msg=""):
    print('|' + now + '| ERROR: ' + colored(msg, 'red'))

def log_notice(msg=""):
    print('|' + now + '| NOTICE: ' + colored(msg, 'magenta'))