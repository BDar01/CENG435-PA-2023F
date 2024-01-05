import socket
from hashlib import md5
from time import time

def receive_tcp(conn):
    # Receive 20 objects (large then small) at a time
    for i in range(20):
        # Initialize data received
        d = b''

        while True:
            # Receive packet on socket
            packet = conn.recv(1024)
            
            # If packet received
            if packet:
                # Append to data
                d += packet  
                # Check for end of file (EOF)
                if b"123c456" in packet:
                    break
            else:
                # Break when no packet received
                break               
        
        # Check if EOF marker is in data
        if (b"123c456" in d):
            # Remove EOF marker from file
            file = d.rstrip(b"123c456")
            
            # Write received files (large or small)
            if i%2 == 0:
                f_name = "large-"+str(int(i//2))
                #print(f_name)
                #with open(f_name, "wb") as f:
                    #f.write(d)
            if i%2 == 1:
                f_name = "small-"+str(int(i//2))
                #print(f_name)
                #with open(f_name, "wb") as f:
                    #f.write(d)

            # Calculate checksum of received file
            #print(f"Checksum: {md5(file).hexdigest()} \n")
            
            # Send Ack message to notify server
            ack = "Ack"
            conn.sendall(ack.encode())

def runClient(index):
    port = 65000+int(index)
    # Create and initalize client socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(1)
        
    # Listen for TCP connection to accept
    conn, _ = sock.accept()     
    receive_tcp(conn)

    # Close connection socket
    conn.close()
    
    # Close client socket
    sock.close()

if __name__ == "__main__":
    total_times = []
    # Take file name
    file_name = input("Enter file name: ")

    # Receive 20 objects 30 times
    for i in range(30):
        print(f"Client No. {i} \n")
        start = time()
        # Send 20 objects
        runClient(i)
        end = time()
        t = end-start
        print(f"Time: {t}s")
        total_times.append(t)

    # Write time (s) to file
    for i in range(30):
        with open(file_name, 'a') as file:
            file.write(f"Time {i}: {total_times[i]:.2f} s\n")

