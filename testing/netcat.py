import argparse
import socket
import subprocess
import sys
import textwrap
import threading

def exec(cmd):
    output = subprocess.check_output(cmd.split(), stderr=subprocess.STDOUT)
    return output.decode('utf-8')

# if we are not listenning, then we act as a client rather than a server, so we attempt to connect to the specified 
# address 
def send(self):
    print("attempting to connect")
    self.sock.connect((self.args.target, int(self.args.port)))

# if listening, then target IP should be my local address, so a socket can be bound to it and listen for incoming 
# connections
def listen(args, server_sock):
    server_sock.bind((args.target, int(args.port)))
    server_sock.listen(5)
    while 1:
        # accept() returns a new socket that we use to communicate with the connected client
        client_socket, addr = server_sock.accept()
        client_thread = threading.Thread(target=handle, args=(args, client_socket,))
        client_thread.start()


def handle(args, client_socket):
    if args.execute:
        output = exec(args.execute)
        client_socket.send(output.encode())
    
    elif args.upload:
        file_buffer = b''
        while 1:
            data = client_socket.recv(4096)
            if data:
                file_buffer += data
                print(f"Length of file: {len(file_buffer)}")
            else:
                break
        
        with open(args.upload, 'wb') as f:
            f.write(file_buffer)
        message = f'Saved file {args.upload}'
        client_socket.send(message.encode())
    
    elif args.command:
        cmd_buffer = b''
        while 1:
            try:
                # 
                client_socket.send(b'#> ')
                while '\n' not in cmd_buffer.decode():
                    cmd_buffer += client_socket.recv(64)
                response = exec(cmd_buffer.decode())
                if response:
                    client_socket.send(response.encode())
                cmd_buffer = b''
            except Exception as e:  
                print(f'Server killed {e}')
                server_sock.close()
                sys.exit()
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Network Tools", formatter_class=argparse.RawDescriptionHelpFormatter,\
        epilog=textwrap.dedent("""
            example:
                netcat.py -t 192.168.1.23 -p 5555 -l -c
        """))
    
    parser.add_argument('-c', '--command', action='store_true', help='sets up command shell')
    parser.add_argument('-e', '--execute', help="execute command")
    parser.add_argument('-l', '--listen', action='store_true', help='indicates that a listener should be set up')
    parser.add_argument('-p', "--port", default=5555, help="port")
    parser.add_argument('-t', '--target', help="Target IP address")
    parser.add_argument('-u', '--upload', help='upload files')
    args = parser.parse_args()

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(args)
    if args.listen:
        buffer = ""
        listen(args, server_sock)
    else:
        print("client mode")
        buffer = sys.stdin.read()
    


    