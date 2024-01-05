import socket
from hashlib import md5

def receive_tcp(conn):
    # Receive 2 objects (large then small) at a time
    for i in range(20):
        d = b''

        while True:
            # Receive packet on socket
            packet = conn.recv(1024)
            
            # If data received
            if packet:
                d += packet  
                if b"123c456" in packet:
                    break
            else:
                break               
        
        if (b"123c456" in d):
            file = d.rstrip(b"123c456")
            # Calculate checksum of received file
            print(f"Checksum {i}: ", md5(file).hexdigest())
            
            if i%2 == 0:
                f_name = "large-"+str(int(i//2))
                print(f_name)
                with open(f_name, "wb") as f:
                    f.write(d)
            if i%2 == 1:
                f_name = "small-"+str(int(i//2))
                print(f_name)
                with open(f_name, "wb") as f:
                    f.write(d)
            
            ack = "Ack"
            conn.sendall(ack.encode())

if __name__ == '__main__':  
    # Create and initalize server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 65002))
    sock.listen(1)
        
    # Listen for TCP connection to accept
    conn, _ = sock.accept()     
    receive_tcp(conn)

    # Close connection socket
    conn.close()
    
    # Close server socket
    sock.close()
