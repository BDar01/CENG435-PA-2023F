import socket
from hashlib import sha256, md5
from time import time
from math import ceil

def createHeader(file_name,marker,num_of_packets):
    header = file_name + "[29,6,28,17,6,20]" + str(marker) + "[29,6,28,17,6,20]" + str(num_of_packets) + "[29,6,28,17,6,20]"
    checksum = md5(header.encode()).hexdigest()
    return header + checksum + "[29,6,28,17,6,20]"

def TCP(ip: str, sender: int, receiver: int):
    file_name1 = "large-0.obj"
    file_name2 = "small-0.obj"

    packet_length = 750  # Define the size of each packet

    file_path = "../../objects/"
    # Open and read file data
    fp1 = open(file_path+file_name1, "rb")
    data1 = fp1.read()
    fp1.close()  # Close the file after reading

    fp2 = open(file_path+file_name2, "rb")
    data2 = fp2.read()
    fp2.close()

    # Calculate number of packets
    packet_count1 = ceil(len(data1)/packet_length)
    packet_count2 = ceil(len(data2)/packet_length)
    
    packets1 = []
    # Split data into packets
    for i in range(packet_count1):
        packets1.append(data1[i * packet_length: (i + 1) * packet_length])
    header1 = createHeader(file_name1, time(), packet_count1)
    
    packets2 = []
    # Split data into packets
    for i in range(packet_count2):
        packets2.append(data1[i * packet_length: (i + 1) * packet_length])
    header2 = createHeader(file_name2, time(), packet_count1)

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    counter = 0

    print("check")

    try:
        # Bind and connect the socket
        s.bind(('0.0.0.0', sender))
        s.connect((ip, receiver))

        print("check2")

        # Send header for file_name1
        s.send(header1.encode())
        print("Header1 sent successfully")

        # Send data packets for file_name1
        print("Packet no:", packet_count1)
        for i in range(packet_count1):
            s.sendall(packets1[i])

        print("Data1 sent successfully")

        # Send header for file_name1
        s.send(header2.encode())
        print("Header2 sent successfully")

        # Send data packets for file_name1
        print("Packet no:", packet_count2)
        for i in range(packet_count2):
            s.sendall(packets2[i])

        print("Data2 sent successfully")

        s.close()
        print("Connection closed")

    except Exception as e:
        print(f"An error occurred: {e}")
       
    
TCP("172.17.0.3", 65000, 65429)