import socket
from math import ceil
from hashlib import md5
from time import time, sleep

def gen_header(f_name,no,t):
    splitter = "[3-20-1-4-88-9-10]"
    # Make header
    h = f_name + splitter + str(t) + splitter + str(no) + splitter
    # Find checksum of header
    c = md5(h.encode()).hexdigest()

    return h + c + splitter

def send_file(sock, f_name):
    d_length = 750
    file_path = "../../objects/"
    
    # Get data from file
    with open(file_path + f_name, "rb") as f:
        d = f.read()

    # Find no. of packets
    p_no = ceil(len(d) / d_length)

    # Create packets from data
    packets = [d[i * d_length: (i + 1) * d_length] for i in range(p_no)]

    # Generate header
    h = gen_header(f_name, p_no, time())

    # Send header
    sock.send(h.encode())

    # Send data packets
    for i in range(p_no):
        sock.sendall(packets[i])

    # Sleep to give time to server before next send_file
    sleep(0.1)

def send_tcp(index, f_name, f_name2):
    ip = "172.17.0.2"
    source = 65004
    dest = 65002

    # Initialize socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    sock.bind(('0.0.0.0', source+int(index)))
    
    # Connect socket
    sock.connect((ip, dest))
    
    # Send 2 files
    send_file(sock, f_name)
    print(f_name)
    send_file(sock, f_name2)
    print(f_name2)

    # Close the socket
    sock.close()
       
    
if __name__ == "__main__":
    # For 20 files:
    file_names = ["large-0.obj", "small-0.obj", "large-1.obj", "small-1.obj", "large-2.obj", "small-2.obj", "large-3.obj", "small-3.obj", "large-4.obj", "small-4.obj", "large-5.obj", "small-5.obj", "large-6.obj", "small-6.obj", "large-7.obj", "small-7.obj", "large-8.obj", "small-8.obj", "large-9.obj", "small-9.obj"]

    for i in range(2):
        # Send 1 large, then 1 small object
        send_tcp(i, file_names[i*2], file_names[i*2+1])
        sleep(0.2)
