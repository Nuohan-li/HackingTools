import subprocess
from misc import * 

print("Hack Terminal")
while(True):
    cmd = input(">>> ")
    match cmd:
        case "portscanner":
            log_info("portscanner is selected")
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
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    log_error("You must provide target IP address")
                else:
                    break
            subprocess.call(['python', 'ftp_anonymous.py', '-i', str(host)])

        case "ftp_brute_force":
            log_info("FTP brute forcer selected")
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


