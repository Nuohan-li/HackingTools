import ftplib
from misc import *
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option('-i', dest='host', help="enter the target device's IP address")
(options, arg) = parser.parse_args()

# TODO: use regex to check IP validity
if options.host == "":
    log_error("You must provide an IP address")
    sys.exit()


# check if we are lucky enough to have a server with ftp anoynomous logon
try:
    ftp = ftplib.FTP(options.host)
    ftp.login("anonymous", "anonymous")
    log_notice(f"Logon succeeded, {options.host} has anonymous login enabled.")
    ftp.quit()
except:
    log_notice(f"Logon failed, {options.host} does NOT have anonymous login enabled")
