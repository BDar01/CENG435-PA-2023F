import socket
from hashlib import sha256


def createHeader(file_name,marker,num_of_packets,p):
    header = file_name + str(p) + str(marker) + str(p) + str(num_of_packets) + str(p)
    checksum = sha256(header.encode()).hexdigest()
    return header + checksum + p


def split_data(data,packet_count):
    """
    :return: list of data split according to the packet sizes
    """
    data_packets = []
    for i in range(int(packet_count)):
        start_index = i 
        end_index = (i + 1) * 750
        data_packet = data[start_index:end_index]
        data_packets.append(data_packet)
    return data_packets

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
    packet_count2 = len(data2) // packet_length + (1 if len(data1) % packet_length else 0)

    # Split data into packets
    packets1 = [data1[i * packet_length:(i + 1) * packet_length] for i in range(packet_count1)]
    packets2 = [data1[i * packet_length:(i + 1) * packet_length] for i in range(packet_count2)]

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
            print(counter)
            counter = counter + 1
            s.sendall(packet)

        print("Data1 sent successfully")
        counter = 0

        for packet in packets2:
            print("counter")
            counter = counter+1
            s.sendall(packet)
        
            print("Data2 sent successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the socket
        s.close()
        print("Connection closed")
       
    
TCP("172.17.0.3", 65428, 65429)