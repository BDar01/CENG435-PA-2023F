import socket
from hashlib import sha256
from time import time

def createHeader(file_name,marker,num_of_packets):
    header = file_name + "[29,6,28,17,6,20]" + str(marker) + "[29,6,28,17,6,20]" + str(num_of_packets) + "[29,6,28,17,6,20]"
    checksum = sha256(header.encode()).hexdigest()
    return header + checksum + "[29,6,28,17,6,20]"

def TCP(ip: str, sender: int, receiver: int):
    file_name1 = "../../objects/large-0.obj"
    file_name2 = "../../objects/small-0.obj"

    packet_length = 750  # Define the size of each packet

    # Open and read file data
    fp1 = open(file_name1, "rb")
    data1 = fp1.read()
    fp1.close()  # Close the file after reading

    fp2 = open(file_name2,"rb")
    data2 = fp2.read()
    fp2.close()

    # Calculate number of packets
    packet_count1 = len(data1) // packet_length + (1 if len(data1) % packet_length else 0)
    packet_count2 = len(data2) // packet_length + (1 if len(data2) % packet_length else 0)

    # Split data into packets
    packets1 = [data1[i * packet_length:(i + 1) * packet_length] for i in range(packet_count1)]
    header1 = createHeader(file_name1, time(), packet_count1)
    packets2 = [data2[i * packet_length:(i + 1) * packet_length] for i in range(packet_count2)]
    header2 = createHeader(file_name2, time(), packet_count2)

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    counter = 0

    print("check")

    try:
        # Bind and connect the socket
        s.bind(('0.0.0.0', sender))
        s.connect((ip, receiver))

        print("check2")

        # Send data packets
        for packet in packets1:
            s.send(header1.encode())
            print(counter)
            counter = counter + 1
            for i in range(packet_count1):
                s.sendall(packets1[i])

        print("Data1 sent successfully")
        counter = 0
        '''
        for packet in packets2:
            s.send(header2.encode())
            print(counter)
            counter = counter + 1
            for i in range(packet_count2):
                s.sendall(packets2[i])
        
            print("Data2 sent successfully")
        '''
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        s.close()
        print("Connection closed")
       
    
TCP("172.17.0.3", 65428, 65429)