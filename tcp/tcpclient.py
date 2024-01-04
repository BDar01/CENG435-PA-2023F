import socket
from hashlib import md5


def get_header(p):
    # Use splitter value of sender to get header values
    splitter = "[3-20-1-4-88-9-10]"
    header = p.split(splitter.encode())

    # Check header format is correct
    if (len(header) >= 4 and header[4:]):
        f_name = header[0].decode()
        p_no = header[1].decode()
        t = header[2].decode()
        c = header[3].decode()

        # Calculate checksum of header
        check = f_name + splitter + p_no + splitter + t + splitter
        hash = md5(check.encode()).hexdigest()

        # Compare calculated checksum with one sent in header
        if (c == hash):
            p_no = int(p_no)
            d = header[4]
            return f_name, p_no, d
        else:
            return None
    else:
            return None

def receive_tcp():
    # Create and initalize server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 65002))
    sock.listen(1)

    # For all 20 objects
    for n in range(1):
        # Listen for TCP connection to accept
        conn, _ = sock.accept()
        # Receive 2 objects (large then small) at a time
        for i in range(2):
            f = b''
            flag = False
            d = []
            f_name = ""
            p_no = 0
            p_count = 0

            while True:
                # Break if all packets received
                if (flag and p_count > p_no):
                    break
                
                # Receive packet on socket
                packet = conn.recv(1024)
                
                # If data received
                if packet:
                    if (not flag):
                        # Check header received properly
                        head = get_header(packet)
                        if (head):
                            flag = True
                            
                            tmp1, tmp2, tmp3 = head
                            f_name = tmp1
                            p_no = tmp2
                            packet = tmp3

                    # Store packets of file
                    if (flag):
                        d.append(packet)
                        p_count += 1
                else:
                    break

            f = b"".join(d)                
            
            # Calculate checksum of received file
            if f_name:
                print(f"Checksum {f_name}: ", md5(f).hexdigest())
        
        # Close connection socket
        conn.close()

    # Close server socket
    sock.close()

if __name__ == '__main__':        
    receive_tcp()
