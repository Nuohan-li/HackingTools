import socket 

port = 3490
host_ip = "192.168.1.32"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_command():
    print("You can now enter commands to send")
    while 1:
        command = input(">>> ")
        if command == "quit":
            target.send(command.encode('utf-8'))
            print("Exiting...")
            break
        else:
            target.send(command.encode('utf-8'))
            result = target.recv(1024)
            print(message.decode('utf-8'))


def server_init():
    global target
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host_ip, port))
    # listen, maximum 10 incoming connections allowed in queue
    sock.listen(10)
    print("Listening for incoming connections")
    # accept returns a socket object that can be used to send/recv to/from remote end
    # also returns address and port bound to the remote end 
    target, ip = sock.accept()
    print(f"Connected with {str(ip)}")
    # sock.close()


server_init()
send_command()