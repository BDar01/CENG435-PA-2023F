import socket
from math import ceil
from hashlib import md5
from time import time, sleep

def send_file(sock, f_name):
    d_length = 750
    file_path = "../../objects/"
    
    # Get data from file
    with open(file_path + f_name, "rb") as f:
        d = f.read()

    end = b"123c456"

    # Send data packets
    sock.sendall(d) 
    sock.sendall(end)

    # Sleep to give time to server before next send_file
    sleep(0.5)


def send_tcp():
    ip = "172.17.0.2"
    source = 65003
    dest = 65002

    # Initialize socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    sock.bind(('0.0.0.0', source))
    
    # Connect socket
    sock.connect((ip, dest))
    
    # For 20 files:
    file_names = ["large-0.obj", "small-0.obj", "large-1.obj", "small-1.obj", "large-2.obj", "small-2.obj", "large-3.obj", "small-3.obj", "large-4.obj", "small-4.obj", "large-5.obj", "small-5.obj", "large-6.obj", "small-6.obj", "large-7.obj", "small-7.obj", "large-8.obj", "small-8.obj", "large-9.obj", "small-9.obj"]

    for i in range(20):
        # Send 1 large, then 1 small object
        send_file(sock, file_names[i])   
        print("Sent: ", file_names[i])

        data = sock.recv(1024).decode()
        print("Ack: ", data)
        

    # Close the socket
    sock.close()
       
    
if __name__ == "__main__":
    send_tcp()
