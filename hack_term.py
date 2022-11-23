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

        case "hasher":
            log_info("Password hasher selected")
            subprocess.call(['python', 'hasher.py'])
        
        case "password_cracker":
            log_info("Password cracker selected")
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


