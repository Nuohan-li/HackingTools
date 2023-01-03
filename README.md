List of available functions

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
           
Details:
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

(The arguments are only needed if the scripts are run directly)

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

