import socket
from hashlib import sha256
from time import time


def decompose(stream, p):
    try:
        streamList = stream.split(p.encode())
        file_name = streamList[0].decode()
        marker = streamList[1].decode()
        packet_count = streamList[2].decode()
        checksum = streamList[3].decode()
    
        partToHash = file_name + p + marker + p + packet_count + p
        hashed_check = sha256(partToHash.encode()).hexdigest()

        if checksum == hashed_check:
            marker = float(marker)
            packet_count = int(packet_count)
            payload = streamList[4]
            return True, file_name, marker, packet_count, payload 
        else:
            return False, None, None, None, None  # Return None for each expected value

    except Exception as e:
        print(f"Decompose error: {e}")  # Optionally print the exception
        return False, None, None, None, None  # Return None for each expected value



def TCP(IP: str, PORT: int):
    file = b''
    isHeaderReceived = False
    accumulator = []
    marker = [0, 0]
    parameter = "[29,6,28,17,6,20]"
    file_name = ""
    packet_count = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S1:
        S1.bind(("", PORT))
        S1.listen()
        print("Waiting for connection...")
        connect, addr = S1.accept()
        with connect:
            print(f"Connected to {addr}")
            while True:
                try:
                    data = connect.recv(1204)
                    if not data:
                        marker[1] = time()
                        break

                    if not isHeaderReceived:
                        try:
                            flag, file_name, marker[0], packet_count, data = decompose(data, parameter)
                            if (flag):
                                isHeaderReceived = True
                            else:
                                file_name = ""
                                packet_count = 0
                                marker[0] = 0

                        except Exception as e:
                            print(f"Error in decompose: {e}")
                            continue

                    accumulator.append(data)
                except socket.timeout:
                    print("Connection timed out")
                    break
                except Exception as e:
                    print(f"Error receiving data: {e}")
                    break

        print("Connection closed.")

        # Calculating time and average
        if marker[1] and marker[0]:
            timeSpent = (marker[1] - marker[0]) * 1000
            avg = timeSpent / int(packet_count) if packet_count else 0
            print(f"Average Time per Packet: {avg} ms")
            print(f"Total Transmission Time: {timeSpent} ms")

        # Merging data and writing to file
        for obj in accumulator:
            file += obj

        if file_name:
            try:
                with open(file_name, "wb") as fp:
                    fp.write(file)
            except FileNotFoundError:
                print(f"Error: File not found - {file_name}")
            except Exception as e:
                print(f"Error writing file: {e}")
        else:
            print("Error: File name is None")

TCP("172.17.0.2", 65429)

""" def TCP(IP:str,PORT:int):
    file = b''
    isItHeader = false
    accumulator = []
    marker = [0,0]
    parameter = [29,6,28,17,6,20]
    S1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        S1.bind(("",PORT))
        S1.listen()

        connect,addr = S1.accept()

        while(True):
            data = connect.recv(1204)
            if(!data)
                marker[1] = time()
                return
            if(!isItHeader)
                try:
                   file_name,marker[0],packet_count,data = decompose(data,parameter)
                   isItHeader = true
                except Exception:
                    pass
            accumulator.append(data)
        
        connect.close()
    
        timeSpent = (marker[1] - marker[0])*1000

        if(packet_count != 0):
            avg = timeSpent/packet_count
        else:
            avg = 0

        for obj in accumulator:
            file += obj

        fp = open(file_name,"wb")
        fp.write(file)
        fp.close()
        

TCP(172.17.0.3,) """