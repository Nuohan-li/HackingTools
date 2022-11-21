from datetime import datetime
from termcolor import colored
import math 
import time
import sys

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

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '_' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r", flush=True)
    # time.sleep(1)


numbers  = [x * 5 for x in range (2000, 3000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))