import sys 
import getopt
import subprocess
import re 
from misc import *

arg_hack_name = ""
arg_ls = ""
arg_help = "{0} -n <name of hack> -l list all hacks".format(sys.argv[0])
arg_list = []
# TODO: need to filter out ip like 256.0.0.0 and so on
ip_regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:lp:i:", ["help", "hack_name=", "list" , "port=", "ip="])
except:
    print(arg_help)
    sys.exit(2)
arg_list = opts
for opt, arg in opts:
    # log_debug('opt is ' + opt + " arg is " + arg)
    if opt in ("-h", "--help"):
        print(arg_help)
        sys.exit(2)
    elif opt in ("-n", "--hack_name"):
        match arg:
            case "portscanner":
                log_info("portscanner selected")
                arg_port = ''
                arg_ip = ''
                
                for _opt,_arg in arg_list:

                    if not '-p' in sys.argv and not '--port' in sys.argv:
                        log_error("Please provide a port number, exiting...")
                        sys.exit(1) 
                    
                    if not '-i' in sys.argv and not '--ip' in sys.argv:
                        log_error("Please provide an IP address, exiting...")
                        sys.exit(1) 

                    if _opt in ("-p", "--port"):
                        # isnumeric() returns true if all chars in string are (0-9)
                        if _arg.isnumeric() and int(_arg) < 65535 and int(_arg) > 0:
                            arg_port = _arg
                        else:
                            log_error("Provided {}. Port must be an integer between 0 and 65535, exiting...".format(_arg))
                            sys.exit(1)
                    if _opt in ("-i", "--ip"):
                        if ip_regex.match(_arg):
                            arg_ip = _arg
                        else:
                            log_error("Provided {}. Invalid IP address provided, exiting...".format(_arg))
                            sys.exit(1)

                subprocess.call(["python", "portscanner.py", "-p {}".format(arg_port), "-i {}".format(arg_ip)])
            case "test1":
                subprocess.call(["python", "test1.py"])
            case "test2":
                subprocess.call(["python", "test2.py"])

    elif opt in ("-l", "--list"):
        arg_ls = arg




# exec(open("portscanner.py").read())
