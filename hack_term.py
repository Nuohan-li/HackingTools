import subprocess
import signal
import os
from ctypes import *

# handles ctrl c
def signal_handler(signum, frame):
    pass
    

signal.signal(signal.SIGINT, signal_handler)


print("HackSuite -> Hacker's toolbox")
print("Type help to see a list of commands")
print("""    
        ,--,                                                                                     
      ,--.'|                           ,-.  .--.--.                            ___               
   ,--,  | :                       ,--/ /| /  /    '.                 ,--,   ,--.'|_             
,---.'|  : '                     ,--. :/ ||  :  /`. /          ,--, ,--.'|   |  | :,'            
|   | : _' |                     :  : ' / ;  |  |--`         ,'_ /| |  |,    :  : ' :            
:   : |.'  |  ,--.--.     ,---.  |  '  /  |  :  ;_      .--. |  | : `--'_  .;__,'  /     ,---.   
|   ' '  ; : /       \   /     \ '  |  :   \  \    `. ,'_ /| :  . | ,' ,'| |  |   |     /     \  
'   |  .'. |.--.  .-. | /    / ' |  |   \   `----.   \|  ' | |  . . '  | | :__,'| :    /    /  | 
|   | :  | ' \__\/: . ..    ' /  '  : |. \  __ \  \  ||  | ' |  | | |  | :   '  : |__ .    ' / | 
'   : |  : ; ," .--.; |'   ; :__ |  | ' \ \/  /`--'  /:  | : ;  ; | '  : |__ |  | '.'|'   ;   /| 
|   | '  ,/ /  /  ,.  |'   | '.'|'  : |--''--'.     / '  :  `--'   \|  | '.'|;  :    ;'   |  / | 
;   : ;--' ;  :   .'   \   :    :;  |,'     `--'---'  :  ,      .-./;  :    ;|  ,   / |   :    | 
|   ,/     |  ,     .-./\   \  / '--'                  `--`----'    |  ,   /  ---`-'   \   \  /  
'---'       `--`---'     `----'                                      ---`-'             `----'                                                            

- Type help to see a detailed help menu
- Type quit to exit the program
- Type list_cmd to see a list of available commands

""")
cmd_buffer = []

while(True):
    cmd = input(">>> ")

    match cmd:
        case "":
            continue

        # Program functionalities
        case "list_cmd":
            cmd_buffer.append("list_cmd")
            print(""" 
Program functions
- help               -- detailed help menu
- quit               -- exit program
- exec_linux_command -- execute Linux command
- list_cmd           -- print this menu 

Hacking Tools
- portscanner        -- Scan ports
- ssh_brute_force    -- Brute force SSH connection
- ftp_anonymous      -- Check if target supports anonymous FTP login
- ftp_brute_force    -- Brute force FTP login
- hasher             -- Hash a password
- password_cracker   -- Crack a hashed password
- MAC_changer        -- Change MAC address of an interface
- netscan            -- Scan the network
- syn_flood          -- Launch flooding attack  
- reverse_shell      -- Open reverse shell command interface

Network Tools
- wiresharpedo       -- Sniff packets
- dns_lookup         -- Return the IP address of a domain name
- find_devices       -- List all network interfaces of the local machine
            """)

        case "help":
            print(""" 
Help menu:
----------------------------------------------------------------------------------------------------------------------
Program Functions:
    -help
        Display this help menu
    
    -list_cmd
        Print a list of supported commands and a brief explanation 

    -quit
        Exit the program 
    
    -exec_linux_command
        Execute Linux command from within this program    -exec_linux_command
    Execute linux command from the program 

Hacking Tools
*The arguments are only needed if the scripts are run directly instead of being run by this program.

    - portscanner
    Scans the specified number of ports, by default it scans all ports
        Mandatory arguments:
            -i: Target IP address
        Optional arguments:
            -p: Protocol that you wish to scan for, if not specified, TCP will be selected
            -r: Number of ports to scan, if not specified, all ports will be scanned

    -ssh_brute_force
    Brute force a SSH session using passwords from the file provided by the user
        Mandatory arguments:
            -i: Target IP address
            -f: Password file location
    
    -ftp_anonymous
    Checks if anonymous login is enabled on the specified host
        Mandatory arguments:
            -i: Target IP address
    
    -ftp_brute_force
    Brute force an FTP session using passwords from the file provided by the user
        Mandatory arguments:
            -i: Target IP address
            -f: Password file location

    -hasher
    Hash a password using the specified hashing algorithm, no arguments, the program will ask users to 
    provide required information upon execution

    -password_cracker
    Crack a hashed password 
        Mandatory arguments:
            -p: hashed password string 
            -h: hashing algorithm
    
    -MAC_changer
    Change the MAC address of a network interface 
        Mandatory arguments:
            -i: interface name
            -m: new MAC address

    -netscan
    Scan the provided network for connected devices
        Mandatory arguments:
            -t: target network IP address

    -syn_flood
    Flood a device with garbage data
        Mandatory arguments:
            -t: Target machine IP address
        Optional arguments:
            -i: Source machine's IP address, default value is this device's IP address
            -p: Source port to send flood
            -s: Size of the payload to send
    
    -arp_spoof:
    ARP spoofer
        Mandatory argument 
            -i: Target machine's IP address
            -r: Router IP address

Network Tools:
    - wire_sharpedo
        Captures network traffic received/sent from all network interfaces and print to the console
    
    - dns_lookup
        Convert a domain name to its corresponding IP address, also IPv6 address if available
        Mandatory argument
            domain_name: domain name
    
    - find_devices
        Find and print all network interfaces of the local machine
        
    
            """)

        case "quit":
            exit()
        
        case "exec_linux_command":
            cmd_buffer.append("exec_linux_command")
            print("You can now enter Linux command, type quit to go back")
            while(True):
                cmd = input("Enter the linux command to execute: ")
                if cmd == "quit":
                    print("\nGoing back")
                    break
                elif cmd[:2] == "cd" and len(cmd) > 1:
                    os.chdir(cmd[3:])
                else:
                    print(f"Command: {cmd.split()}")
                    subprocess.call(cmd.split())
                
# hacking tools
        case "portscanner":
            print("portscanner is selected")
            cmd_buffer.append("portscanner")
            while(True):
                ip = input(">>> Enter target IP address: ")
                if ip == '':
                    print("You must provide an IP address")
                else:
                    break
                
            protocol = input(">>> Enter the protocol the port is running, default is TCP: ")
            ports = input(">>> Enter the number of ports to scan, default scans all ports: ")
            
            subprocess.call(['python3', 'portscan.py', '-p', str(protocol), '-i', str(ip), '-r', str(ports)])
        
        case "ssh_brute_force":
            print("SSH brute forcer selected")
            cmd_buffer.append("ssh_brute_force")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    print("You must provide target IP address")
                else: 
                    break
            while(True):
                file_location = input(">>> Enter password file location: ")
                if file_location == "":
                    print("You must provide file location")
                else: 
                    break
            subprocess.call(['python3', 'ssh_brute_force.py', '-i', str(host), '-f', str(file_location)])

        case "ftp_anonymous":
            print("Check if host host has FTP anonymous login enabled")
            cmd_buffer.append("ftp_anonymous")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    print("You must provide target IP address")
                else:
                    break
            subprocess.call(['python33', 'ftp_anonymous.py', '-i', str(host)])

        case "ftp_brute_force":
            print("FTP brute forcer selected")
            cmd_buffer.append("ftp_brute_force")
            while(True):
                host = input(">>> Enter target IP address: ")
                if host == "":
                    print("You must provide target IP address")
                else: 
                    break
            while(True):
                file_location = input(">>> Enter password file location: ")
                if file_location == "":
                    print("You must provide file location")
                else: 
                    break
            subprocess.call(['python3', 'ftp_brute_force.py', '-i', str(host), '-f', str(file_location)])

        case "hasher":
            print("Password hasher selected")
            cmd_buffer.append("hasher")
            subprocess.call(['python3', 'hasher.py'])
        
        case "password_cracker":
            print("Password cracker selected")
            cmd_buffer.append("password_cracker")
            while(True):
                hashed = input(">>> Enter a hashed password: ")
                if hashed == "":
                    print("You must provide a hashed password")
                else: 
                    break
            while(True):
                hash_algo = input(">>> Enter a hashing algorithm: ")
                if hash_algo == "":
                    print("You must provide a hashing algorithm")
                else: 
                    break
            subprocess.call(['python3', 'password_cracker.py', '-p', hashed, '-a', hash_algo])
        
        case "MAC_changer":
            print("interface MAC address changer selected")
            cmd_buffer.append("MAC_changer")
            while(True):
                interface = input(">>> Enter an interface: ")
                if interface == "":
                    print("You must provide a interface whose MAC address you wish to change")
                else: 
                    break
            while(True):
                mac = input(">>> Enter the new MAC address: ")
                if mac == "":
                    print("You must provide a new MAC address")
                else: 
                    break
            subprocess.call(['python3', 'MAC_changer.py', '-i', interface, '-m', mac])
        
        case "netscan":
            print("Network scanner selected")
            cmd_buffer.append("netscan")
            while(True):
                prefix = input(">>> Enter IP address of a network to scan: ")
                if prefix == "":
                    print("You must provide an IP address")
                else: 
                    break
            subprocess.call(['python3', 'netscan.py', '-t', prefix])
        
        case "syn_flood":
            cmd_buffer.append("syn_flood")
            while(True):
                dst = input(">>> Enter the target IP address: ")
                if dst == "":
                    print("You must provide a target IP address")
                else:
                    break
            src = input(">>> Enter the source IP address, default=this device's IP ")
            sport = input(">>> Enter a port to send flood, default=20 ")
            load_size = input(">>> Enter the size of the payload, default=100 ")

            subprocess.call(['python', 'syn_flood.py', '-t', dst, '-i', src, '-p', sport, '-s', load_size])
        
        case "arp_spoof":
            cmd_buffer.append("arp_spoof")
            while(True):
                target_ip = input(">>> Enter the target IP address: ")
                if target_ip == "":
                    print("You must provide a target IP address")
                else:
                    break
            while(True):
                router_ip = input(">>> Enter the router IP address: ")
                if router_ip == "":
                    print("You must provide a router IP address")
                else:
                    break

            subprocess.call(['python', 'syn_flood.py', '-i', target_ip, '-r', router_ip])
        
        case "reverse_shell":
            print("not supported yet")
        
# Network tools
        # TODO: using ctypes to call the function
        case "wire_sharpedo":
            subprocess.call(["./wire_sharpedo"])

        case "find_devices":
            subprocess.call(['./network_tools/find_dev'])
        
        case "dns_lookup":
            while(True):
                domain_name = input(">>> Enter a domain name: ")
                if domain_name == "":
                    print("You must provide a domain name")
                else:
                    break
            subprocess.call(['./network_tools/dns_lookup', domain_name])
        
        case _:
            print("This command does not exist, type list_cmd to see a list of commands")


                


