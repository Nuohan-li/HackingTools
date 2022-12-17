
from __future__ import print_function
from datetime import datetime
import time
import sys

now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def progress(progress, total):
    percent = 100 * (progress / float(total))
    # bar = '#' * int(percent) + '_' * (100 - int(percent))
    # print(f"|{bar}|", end="\r") 
    # sys.stdout.flush()
    print(f"Current progress: {percent:.2f}%", end="\r")
    sys.stdout.flush()