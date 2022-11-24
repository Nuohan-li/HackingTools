import subprocess
import signal
from misc import * 

def signal_handler(signum, frame):
    pass
    

signal.signal(signal.SIGINT, signal_handler)


print("HackingSuite -> Hacker's toolbox")
print("Type help to see a list of commands")
cmd_buffer = []
while(True):
    cmd = input(">>> ")

    match cmd:
        case "help":
            pass
        
        case "quit":
            print("Exiting...")
            sys.exit()

        case "portscanner":
            log_info("portscanner is selected")
            cmd_buffer.append("portscanner")
            while(True):
                ip = input(">>> Enter target IP address: ")
                if ip == '':
                    log_error("You must provide an IP address")
                else:
                    break
                
            protocol = input(">>> Enter the protocol the port is running, default is TCP: ")
            ports = input(">>> Enter the number of ports to scan, default scans all ports: ")
            
            subprocess.call(['python', 'portscan.py', '-p', str(protocol), '-i', str(ip), '-r', str(ports)])
        
        case "ssh_brute_force":
            log_info("SSH brute forcer selected")
            cmd_buffer.append("ssh_brute_force")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    log_error("You must provide target IP address")
                else: 
                    break
            while(True):
                file_location = input(">>> Enter password file location: ")
                if file_location == "":
                    log_error("You must provide file location")
                else: 
                    break
            subprocess.call(['python', 'ssh_brute_force.py', '-i', str(host), '-f', str(file_location)])

        case "ftp_anonymous":
            log_info("Check if host host has FTP anonymous login enabled")
            cmd_buffer.append("ftp_anonymous")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    log_error("You must provide target IP address")
                else:
                    break
            subprocess.call(['python', 'ftp_anonymous.py', '-i', str(host)])

        case "ftp_brute_force":
            log_info("FTP brute forcer selected")
            cmd_buffer.append("ftp_brute_force")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    log_error("You must provide target IP address")
                else: 
                    break
            while(True):
                file_location = input(">>> Enter password file location: ")
                if file_location == "":
                    log_error("You must provide file location")
                else: 
                    break
            subprocess.call(['python', 'ftp_brute_force.py', '-i', str(host), '-f', str(file_location)])

        case "hasher":
            log_info("Password hasher selected")
            cmd_buffer.append("hasher")
            subprocess.call(['python', 'hasher.py'])
        
        case "password_cracker":
            log_info("Password cracker selected")
            cmd_buffer.append("password_cracker")
            while(True):
                hashed = input(">>> Enter a hashed password: ")
                if hashed == "":
                    log_error("You must provide a hashed password")
                else: 
                    break
            while(True):
                hash_algo = input(">>> Enter a hashing algorithm: ")
                if hash_algo == "":
                    log_error("You must provide a hashing algorithm")
                else: 
                    break
            subprocess.call(['python', 'password_cracker.py', '-p', hashed, '-a', hash_algo])
        
        case "MAC_changer":
            log_info("interface MAC address changer selected")
            cmd_buffer.append("MAC_changer")
            while(True):
                interface = input(">>> Enter an interface: ")
                if interface == "":
                    log_error("You must provide a interface whose MAC address you wish to change")
                else: 
                    break
            while(True):
                mac = input(">>> Enter the new MAC address: ")
                if mac == "":
                    log_error("You must provide a new MAC address")
                else: 
                    break
            subprocess.call(['python', 'MAC_changer.py', '-i', interface, '-m', mac])
        
        case "exec_linux_command":
            cmd_buffer.append("exec_linux_command")
            while(True):
                try:
                    cmd = input("Enter the linux command to execute: ")
                    subprocess.call(cmd.split())
                except KeyboardInterrupt:
                    log_info("\nGoing back")
                    break
        
        case "syn_flood":
            cmd_buffer.append("syn_flood")
            while(True):
                dst = input(">>> Enter the target IP address: ")
                if dst == "":
                    log_error("You must provide a target IP address")
                else:
                    break
            src = input(">>> Enter the source IP address, default=this device's IP: ")
            sport = input(">>> Enter a port to send flood, default=20: ")
            load_size = input(">>> Enter the size of the payload, default=100: ")

            subprocess.call(['python', 'syn_flood.py', '-t', dst, '-i', src, '-p', sport, '-s', load_size])

        case _:
            log_error("This command does not exist, type help to see a list of commands")


                


