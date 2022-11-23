from urllib.request import urlopen
import hashlib
import optparse
import sys
from misc import *

parser = optparse.OptionParser()
parser.add_option('-p', dest='hash_value', help="enter a hashed password")
parser.add_option('-a', dest="hash_algo", help="enter a hashing algorithm")
(options, arg) = parser.parse_args()

if not options.hash_value:
    log_error("You must enter a hashed password to be cracked")
    sys.exit()

if not options.hash_algo:
    log_error("You must provide a hashing algorithm")
    sys.exit()

hashed = options.hash_value
hash_algo = options.hash_algo
password_list = str(urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt").read(), 'utf-8')

############################################
# args
# password_list: a list of password to check against
# hash_algo: specify a hashing algorithm 
# hashed: a hashed password to be checked against
#
##########################################

def check_password(password_list, hash_algo, hashed):
    if hash_algo == "md5":
        for password in password_list.split('\n'):
            password_hash = hashlib.md5()
            password_hash.update(password.encode())
            hashguess = password_hash.hexdigest()
            if str(hashguess) == str(hashed):
                log_info(f"Password matched! It is {str(password)}")
                return 1
    elif hash_algo == "sha1":
        for password in password_list.split('\n'):
            password_hash = hashlib.sha1()
            password_hash.update(password.encode())
            hashguess = password_hash.hexdigest()
            if str(hashguess) == str(hashed):
                log_info(f"Password matched! It is {str(password)}")
                return 1
    elif hash_algo == "sha224":
        for password in password_list.split('\n'):
            password_hash = hashlib.sha224()
            password_hash.update(password.encode())
            hashguess = password_hash.hexdigest()
            if str(hashguess) == str(hashed):
                log_info(f"Password matched! It is {str(password)}")
                return 1
    elif hash_algo == "sha256":
        for password in password_list.split('\n'):
            password_hash = hashlib.sha256()
            password_hash.update(password.encode())
            hashguess = password_hash.hexdigest()
            if str(hashguess) == str(hashed):
                log_info(f"Password matched! It is {str(password)}")
                return 1
    elif hash_algo == "sha512":
        for password in password_list.split('\n'):
            password_hash = hashlib.sha512()
            password_hash.update(password.encode())
            hashguess = password_hash.hexdigest()
            if str(hashguess) == str(hashed):
                log_info(f"Password matched! It is {str(password)}")
                return 1
    

if check_password(password_list, hash_algo, hashed):
    log_notice("Password matched successfully")
else:
    log_notice("Provided password does not match any password in the list")

