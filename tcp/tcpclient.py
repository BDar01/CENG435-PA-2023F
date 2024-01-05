import socket
from hashlib import md5

'''
def get_header(p):
    # Use splitter value of sender to get header values
    splitter = "[3-20-1-4-88-9-10]"
    header = p.split(splitter.encode())

    # Check header format is correct
    if (len(header) >= 4 and header[4:]):
        f_name = header[0].decode()
        t = header[1].decode()
        p_no = header[2].decode()
        c = header[3].decode()

        # Calculate checksum of header
        check = f_name + splitter + t + splitter + p_no + splitter
        hash = md5(check.encode()).hexdigest()

        # Compare calculated checksum with one sent in header
        if (c == hash):
            p_no = int(p_no)
            d = header[4]
            return f_name, p_no, d
        else:
            return False
    else:
            return False
'''

def receive_tcp(conn):
    # Receive 2 objects (large then small) at a time
    for i in range(2):
        d = []

        while True:
            # Receive packet on socket
            packet = conn.recv(1024)
            
            # If data received
            if packet:
                d += packet  
                if "123" in packet.decode():
                    break
            else:
                break               
        
        data = d.decode()
        if (data.strip("123")):
            f = data.rstrip("123")
            # Calculate checksum of received file
            print(f"Checksum {f_name}: ", md5(f).hexdigest())

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
