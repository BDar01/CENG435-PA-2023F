import socket
from math import ceil
from hashlib import md5
from time import time, sleep

def gen_header(f_name,t,no):
    # Make header
    h = f_name + "[3-20-1-4-88-9-10]" + str(no) + "[3-20-1-4-88-9-10]" + str(t) + "[3-20-1-4-88-9-10]"
    # Find checksum of header
    c = md5(h.encode()).hexdigest()

    return h + c + "[3-20-1-4-88-9-10]"

def send_file(sock, f_name):
    d_length = 750
    file_path = "../../objects/"
    
    # Get data from file
    with open(file_path + f_name, "rb") as f:
        d = f.read()

    # Find no. of packets
    p_no = ceil(len(d) / d_length)

    # Create packets from data
    packets = [d[i * p_no: (i + 1) * d_length] for i in range(p_no)]

    # Generate header
    h = gen_header(f_name, time(), p_no)

    # Send header
    sock.send(h.encode())

    # Send data packets
    for i in range(p_no):
        sock.sendall(packets[i])

    # Sleep to give time to server before next send_file
    sleep(0.1)

def send_tcp(ip, source, dest, index):

    # List of file names
    file_names = ["large-0.obj", "small-0.obj", "large-1.obj", "small-1.obj", "large-2.obj", "small-2.obj", "large-3.obj", "small-3.obj", "large-4.obj", "small-4.obj", "large-5.obj", "small-5.obj", "large-6.obj", "small-6.obj", "large-7.obj", "small-7.obj", "large-8.obj", "small-8.obj", "large-9.obj", "small-9.obj"]

    # Initialize socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    sock.bind(('0.0.0.0', source))
    
    # Connect socket
    sock.connect((ip, dest))
    
    # Send 2 files
    send_file(sock, file_names[index])
    send_file(sock, file_names[index+1])
    
    # Close the socket
    sock.close()
       
    
if __name__ == "__main__":
    # For 20 files:
    for i in range(10):
        # Send 1 large, then 1 small object
        send_tcp("172.17.0.3", 65001, 65002, i)
        sleep(0.5)