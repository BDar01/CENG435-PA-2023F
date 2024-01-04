import socket
from hashlib import sha256, md5
from time import time, sleep
from math import ceil

def createHeader(file_name,marker,num_of_packets):
    header = file_name + "[29,6,28,17,6,20]" + str(marker) + "[29,6,28,17,6,20]" + str(num_of_packets) + "[29,6,28,17,6,20]"
    checksum = md5(header.encode()).hexdigest()
    return header + checksum + "[29,6,28,17,6,20]"

def send_file(s, file_name):
    packet_length = 750
    file_path = "../../objects/"
    # Open and read file data
    with open(file_path + file_name, "rb") as file:
        data = file.read()

    # Calculate number of packets
    packet_count = ceil(len(data) / packet_length)

    # Split data into packets
    packets = [data[i * packet_length: (i + 1) * packet_length] for i in range(packet_count)]

    # Create header
    header = createHeader(file_name, time(), packet_count)

    # Send header
    s.send(header.encode())
    print(f"Header for {file_name} sent successfully")

    # Send data packets
    for i in range(packet_count):
        s.sendall(packets[i])

    print(f"Data for {file_name} sent successfully")
    sleep(0.1)

def TCP(ip: str, sender: int, receiver: int):
    '''
    file_name1 = "large-0.obj"
    file_name2 = "small-0.obj"
    file_name3 = "large-1.obj"
    file_name4 = "small-1.obj"
    file_name5 = "large-2.obj"
    file_name6 = "small-2.obj"
    file_name7 = "large-3.obj"
    file_name8 = "small-3.obj"
    file_name9 = "large-4.obj"
    file_name10 = "small-4.obj"
    file_name11 = "large-5.obj"
    file_name12 = "small-5.obj"
    file_name13 = "large-6.obj"
    file_name14 = "small-6.obj"
    file_name15 = "large-7.obj"
    file_name16 = "small-7.obj"
    file_name17 = "large-8.obj"
    file_name18 = "small-8.obj"
    file_name19 = "large-9.obj"
    file_name20 = "small-9.obj"

    packet_length = 750  # Define the size of each packet

    file_path = "../../objects/"

    # large-0.obj
    # Open and read file data
    fp1 = open(file_path+file_name1, "rb")
    data1 = fp1.read()
    fp1.close()  # Close the file after reading

    # Calculate number of packets
    packet_count1 = ceil(len(data1)/packet_length)

    packets1 = []
    # Split data into packets
    for i in range(packet_count1):
        packets1.append(data1[i * packet_length: (i + 1) * packet_length])
    header1 = createHeader(file_name1, time(), packet_count1)

    # small-0.obj
    # Open and read file data
    fp2 = open(file_path+file_name2, "rb")
    data2 = fp2.read()
    fp2.close()

    # Calculate number of packets
    packet_count2 = ceil(len(data2)/packet_length)
    
    packets2 = []
    # Split data into packets
    for i in range(packet_count2):
        packets2.append(data2[i * packet_length: (i + 1) * packet_length])
    header2 = createHeader(file_name2, time(), packet_count2)

    # large-1.obj
    # Open and read file data
    fp3 = open(file_path+file_name3, "rb")
    data3 = fp3.read()
    fp3.close()  # Close the file after reading

    # Calculate number of packets
    packet_count3 = ceil(len(data3)/packet_length)

    packets3 = []
    # Split data into packets
    for i in range(packet_count3):
        packets3.append(data3[i * packet_length: (i + 1) * packet_length])
    header3 = createHeader(file_name3, time(), packet_count3)

    # small-1.obj
    # Open and read file data
    fp4 = open(file_path+file_name4, "rb")
    data4 = fp4.read()
    fp4.close()

    # Calculate number of packets
    packet_count4 = ceil(len(data4)/packet_length)
    
    packets4 = []
    # Split data into packets
    for i in range(packet_count4):
        packets4.append(data4[i * packet_length: (i + 1) * packet_length])
    header4 = createHeader(file_name4, time(), packet_count4)

    # large-2.obj
    # Open and read file data
    fp5 = open(file_path+file_name5, "rb")
    data5 = fp5.read()
    fp5.close()  # Close the file after reading

    # Calculate number of packets
    packet_count5 = ceil(len(data5)/packet_length)

    packets5 = []
    # Split data into packets
    for i in range(packet_count5):
        packets5.append(data5[i * packet_length: (i + 1) * packet_length])
    header5 = createHeader(file_name5, time(), packet_count5)

    # small-2.obj
    # Open and read file data
    fp6 = open(file_path+file_name6, "rb")
    data6 = fp6.read()
    fp6.close()

    # Calculate number of packets
    packet_count6 = ceil(len(data6)/packet_length)
    
    packets6 = []
    # Split data into packets
    for i in range(packet_count6):
        packets6.append(data6[i * packet_length: (i + 1) * packet_length])
    header6 = createHeader(file_name6, time(), packet_count6)

    # large-3.obj
    # Open and read file data
    fp7 = open(file_path+file_name7, "rb")
    data7 = fp7.read()
    fp7.close()  # Close the file after reading

    # Calculate number of packets
    packet_count7 = ceil(len(data7)/packet_length)

    packets7 = []
    # Split data into packets
    for i in range(packet_count7):
        packets7.append(data7[i * packet_length: (i + 1) * packet_length])
    header7 = createHeader(file_name7, time(), packet_count7)

    # small-3.obj
    # Open and read file data
    fp8 = open(file_path+file_name8, "rb")
    data8 = fp8.read()
    fp8.close()

    # Calculate number of packets
    packet_count8 = ceil(len(data8)/packet_length)
    
    packets8 = []
    # Split data into packets
    for i in range(packet_count8):
        packets8.append(data8[i * packet_length: (i + 1) * packet_length])
    header8 = createHeader(file_name8, time(), packet_count8)

    # large-4.obj
    # Open and read file data
    fp9 = open(file_path+file_name9, "rb")
    data9 = fp9.read()
    fp9.close()  # Close the file after reading

    # Calculate number of packets
    packet_count9 = ceil(len(data9)/packet_length)

    packets9 = []
    # Split data into packets
    for i in range(packet_count9):
        packets9.append(data9[i * packet_length: (i + 1) * packet_length])
    header9 = createHeader(file_name9, time(), packet_count9)

    # small-4.obj
    # Open and read file data
    fp10 = open(file_path+file_name10, "rb")
    data10 = fp10.read()
    fp10.close()

    # Calculate number of packets
    packet_count10 = ceil(len(data10)/packet_length)
    
    packets10 = []
    # Split data into packets
    for i in range(packet_count10):
        packets10.append(data10[i * packet_length: (i + 1) * packet_length])
    header10 = createHeader(file_name10, time(), packet_count10)

    # large-5.obj
    # Open and read file data
    fp11 = open(file_path+file_name11, "rb")
    data11 = fp11.read()
    fp11.close()  # Close the file after reading

    # Calculate number of packets
    packet_count11 = ceil(len(data11)/packet_length)

    packets11 = []
    # Split data into packets
    for i in range(packet_count11):
        packets11.append(data11[i * packet_length: (i + 1) * packet_length])
    header11 = createHeader(file_name11, time(), packet_count11)

    # small-5.obj
    # Open and read file data
    fp12 = open(file_path+file_name12, "rb")
    data12 = fp12.read()
    fp12.close()

    # Calculate number of packets
    packet_count12 = ceil(len(data12)/packet_length)
    
    packets12 = []
    # Split data into packets
    for i in range(packet_count12):
        packets12.append(data12[i * packet_length: (i + 1) * packet_length])
    header12 = createHeader(file_name12, time(), packet_count12)

    # large-6.obj
    # Open and read file data
    fp13 = open(file_path+file_name13, "rb")
    data13 = fp13.read()
    fp13.close()  # Close the file after reading

    # Calculate number of packets
    packet_count13 = ceil(len(data13)/packet_length)

    packets13 = []
    # Split data into packets
    for i in range(packet_count13):
        packets13.append(data13[i * packet_length: (i + 1) * packet_length])
    header13 = createHeader(file_name13, time(), packet_count13)

    # small-6.obj
    # Open and read file data
    fp14 = open(file_path+file_name14, "rb")
    data14 = fp14.read()
    fp14.close()

    # Calculate number of packets
    packet_count14 = ceil(len(data14)/packet_length)
    
    packets14 = []
    # Split data into packets
    for i in range(packet_count14):
        packets14.append(data14[i * packet_length: (i + 1) * packet_length])
    header14 = createHeader(file_name14, time(), packet_count14)
    
    # large-7.obj
    # Open and read file data
    fp15 = open(file_path+file_name15, "rb")
    data15 = fp15.read()
    fp15.close()  # Close the file after reading

    # Calculate number of packets
    packet_count15 = ceil(len(data15)/packet_length)

    packets15 = []
    # Split data into packets
    for i in range(packet_count15):
        packets15.append(data15[i * packet_length: (i + 1) * packet_length])
    header15 = createHeader(file_name15, time(), packet_count15)

    # small-7.obj
    # Open and read file data
    fp16 = open(file_path+file_name16, "rb")
    data16 = fp16.read()
    fp16.close()

    # Calculate number of packets
    packet_count16 = ceil(len(data16)/packet_length)
    
    packets16 = []
    # Split data into packets
    for i in range(packet_count16):
        packets16.append(data16[i * packet_length: (i + 1) * packet_length])
    header16 = createHeader(file_name16, time(), packet_count16)

    # large-8.obj
    # Open and read file data
    fp17 = open(file_path+file_name17, "rb")
    data17 = fp17.read()
    fp17.close()  # Close the file after reading

    # Calculate number of packets
    packet_count17 = ceil(len(data17)/packet_length)

    packets17 = []
    # Split data into packets
    for i in range(packet_count17):
        packets17.append(data17[i * packet_length: (i + 1) * packet_length])
    header17 = createHeader(file_name17, time(), packet_count17)

    # small-8.obj
    # Open and read file data
    fp18 = open(file_path+file_name18, "rb")
    data18 = fp18.read()
    fp18.close()

    # Calculate number of packets
    packet_count18 = ceil(len(data18)/packet_length)
    
    packets18 = []
    # Split data into packets
    for i in range(packet_count18):
        packets18.append(data18[i * packet_length: (i + 1) * packet_length])
    header18 = createHeader(file_name18, time(), packet_count18)

    # large-9.obj
    # Open and read file data
    fp19 = open(file_path+file_name19, "rb")
    data19 = fp19.read()
    fp19.close()  # Close the file after reading

    # Calculate number of packets
    packet_count19 = ceil(len(data19)/packet_length)

    packets19 = []
    # Split data into packets
    for i in range(packet_count19):
        packets19.append(data19[i * packet_length: (i + 1) * packet_length])
    header19 = createHeader(file_name19, time(), packet_count19)

    # small-9.obj
    # Open and read file data
    fp20 = open(file_path+file_name20, "rb")
    data20 = fp20.read()
    fp20.close()

    # Calculate number of packets
    packet_count20 = ceil(len(data20)/packet_length)
    
    packets20 = []
    # Split data into packets
    for i in range(packet_count20):
        packets20.append(data20[i * packet_length: (i + 1) * packet_length])
    header20 = createHeader(file_name20, time(), packet_count20)
    '''

    # List of file names
    file_names = ["large-0.obj", "small-0.obj"]#, "large-1.obj", "small-1.obj", "large-2.obj", "small-2.obj", "large-3.obj", "small-3.obj", "large-4.obj", "small-4.obj", "large-5.obj", "small-5.obj", "large-6.obj", "small-6.obj", "large-7.obj", "small-7.obj", "large-8.obj", "small-8.obj", "large-9.obj", "small-9.obj"]

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind and connect the socket
        s.bind(('0.0.0.0', sender))
        s.connect((ip, receiver))
        
        for f in file_names:
            send_file(s, f)
        
        '''
        # Send header for file_name1
        s.send(header1.encode())
        print(f"Header1 length {len(header1.encode())} sent successfully")

        # Send data packets for file_name1
        print("Packet no:", packet_count1)
        for i in range(packet_count1):
            s.sendall(packets1[i])

        print("Data1 sent successfully")

        sleep(0.1)

        # Send header for file_name2
        s.send(header2.encode())
        print(f"Header2 length {len(header2.encode())} sent successfully")

        # Send data packets for file_name2
        print("Packet no:", packet_count2)
        for i in range(packet_count2):
            s.sendall(packets2[i])

        print("Data2 sent successfully")
        
        sleep(0.1)

        # Send header for file_name3
        s.send(header3.encode())
        print(f"Header3 length {len(header3.encode())} sent successfully")

        # Send data packets for file_name3
        print("Packet no:", packet_count3)
        for i in range(packet_count3):
            s.sendall(packets3[i])

        print("Data3 sent successfully")
        
        sleep(0.1)

        # Send header for file_name4
        s.send(header4.encode())
        print(f"Header4 length {len(header4.encode())} sent successfully")

        # Send data packets for file_name4
        print("Packet no:", packet_count4)
        for i in range(packet_count4):
            s.sendall(packets4[i])

        print("Data4 sent successfully")

        sleep(0.1)
        
        # Send header for file_name5
        s.send(header5.encode())
        print(f"Header5 length {len(header5.encode())} sent successfully")

        # Send data packets for file_name5
        print("Packet no:", packet_count5)
        for i in range(packet_count5):
            s.sendall(packets5[i])

        print("Data5 sent successfully")

        sleep(0.1)

        # Send header for file_name6
        s.send(header6.encode())
        print(f"Header6 length {len(header6.encode())} sent successfully")

        # Send data packets for file_name6
        print("Packet no:", packet_count6)
        for i in range(packet_count6):
            s.sendall(packets6[i])

        print("Data6 sent successfully")

        sleep(0.1)

        # Send header for file_name7
        s.send(header7.encode())
        print(f"Header7 length {len(header7.encode())} sent successfully")

        # Send data packets for file_name7
        print("Packet no:", packet_count7)
        for i in range(packet_count7):
            s.sendall(packets7[i])

        print("Data7 sent successfully")

        sleep(0.1)

        # Send header for file_name8
        s.send(header8.encode())
        print(f"Header8 length {len(header8.encode())} sent successfully")

        # Send data packets for file_name8
        print("Packet no:", packet_count8)
        for i in range(packet_count8):
            s.sendall(packets8[i])

        print("Data8 sent successfully")
        
        sleep(0.1)

        # Send header for file_name9
        s.send(header9.encode())
        print(f"Header9 length {len(header9.encode())} sent successfully")

        # Send data packets for file_name9
        print("Packet no:", packet_count9)
        for i in range(packet_count9):
            s.sendall(packets9[i])

        print("Data9 sent successfully")

        sleep(0.1)

        # Send header for file_name10
        s.send(header10.encode())
        print(f"Header10 length {len(header10.encode())} sent successfully")

        # Send data packets for file_name10
        print("Packet no:", packet_count10)
        for i in range(packet_count10):
            s.sendall(packets10[i])

        print("Data10 sent successfully")

        sleep(0.1)

        # Send header for file_name11
        s.send(header11.encode())
        print(f"Header11 length {len(header11.encode())} sent successfully")

        # Send data packets for file_name11
        print("Packet no:", packet_count11)
        for i in range(packet_count11):
            s.sendall(packets11[i])

        print("Data11 sent successfully")

        sleep(0.1)

        # Send header for file_name12
        s.send(header12.encode())
        print(f"Header12 length {len(header12.encode())} sent successfully")

        # Send data packets for file_name12
        print("Packet no:", packet_count12)
        for i in range(packet_count12):
            s.sendall(packets12[i])

        print("Data12 sent successfully")

        sleep(0.1)

        # Send header for file_name13
        s.send(header13.encode())
        print(f"Header13 length {len(header13.encode())} sent successfully")

        # Send data packets for file_name13
        print("Packet no:", packet_count13)
        for i in range(packet_count13):
            s.sendall(packets13[i])

        print("Data13 sent successfully")

        sleep(0.1)

        # Send header for file_name14
        s.send(header14.encode())
        print(f"Header14 length {len(header14.encode())} sent successfully")

        # Send data packets for file_name14
        print("Packet no:", packet_count14)
        for i in range(packet_count14):
            s.sendall(packets14[i])

        print("Data14 sent successfully")

        sleep(0.1)

        # Send header for file_name15
        s.send(header15.encode())
        print(f"Header15 length {len(header15.encode())} sent successfully")

        # Send data packets for file_name15
        print("Packet no:", packet_count15)
        for i in range(packet_count15):
            s.sendall(packets15[i])

        print("Data15 sent successfully")

        sleep(0.1)

        # Send header for file_name16
        s.send(header16.encode())
        print(f"Header16 length {len(header16.encode())} sent successfully")

        # Send data packets for file_name16
        print("Packet no:", packet_count16)
        for i in range(packet_count16):
            s.sendall(packets16[i])

        print("Data16 sent successfully")

        sleep(0.1)

        # Send header for file_name17
        s.send(header17.encode())
        print(f"Header17 length {len(header17.encode())} sent successfully")

        # Send data packets for file_name17
        print("Packet no:", packet_count17)
        for i in range(packet_count17):
            s.sendall(packets17[i])

        print("Data17 sent successfully")

        sleep(0.1)

        # Send header for file_name18
        s.send(header18.encode())
        print(f"Header18 length {len(header18.encode())} sent successfully")

        # Send data packets for file_name18
        print("Packet no:", packet_count18)
        for i in range(packet_count18):
            s.sendall(packets18[i])

        print("Data18 sent successfully")

        sleep(0.1)

        # Send header for file_name19
        s.send(header19.encode())
        print(f"Header19 length {len(header19.encode())} sent successfully")

        # Send data packets for file_name19
        print("Packet no:", packet_count19)
        for i in range(packet_count19):
            s.sendall(packets19[i])

        print("Data19 sent successfully")

        sleep(0.1)

        # Send header for file_name20
        s.send(header20.encode())
        print(f"Header20 length {len(header20.encode())} sent successfully")

        # Send data packets for file_name20
        print("Packet no:", packet_count20)
        for i in range(packet_count20):
            s.sendall(packets20[i])

        print("Data20 sent successfully")
        '''
        s.close()
        print("Connection closed")

    except Exception as e:
        print(f"An error occurred: {e}")
       
    
TCP("172.17.0.3", 65000, 65429)