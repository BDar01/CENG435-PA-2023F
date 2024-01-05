import socket
from time import sleep

def send_file(sock, f_name):
    # Send from root dir containing "objects"
    file_path = "../../objects/"
    
    # Get data from file
    with open(file_path + f_name, "rb") as f:
        d = f.read()

    # Make end to denote end of file
    end = b"123c456"

    # Send file to client
    sock.sendall(d) 
    # Append end to file to inform server
    sock.sendall(end)

    # Sleep to give time to server before next send_file
    sleep(0.5)


def send_tcp(index):
    ip = "172.17.0.2"
    source = 65001+int(index)
    dest = 65000+int(index)

    # Initialize socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    sock.bind(('0.0.0.0', source))
    
    # Connect socket
    sock.connect((ip, dest))
    
    # For 20 files, send 1 large, then 1 small object
    file_names = ["large-0.obj", "small-0.obj", "large-1.obj", "small-1.obj", "large-2.obj", "small-2.obj", "large-3.obj", "small-3.obj", "large-4.obj", "small-4.obj", "large-5.obj", "small-5.obj", "large-6.obj", "small-6.obj", "large-7.obj", "small-7.obj", "large-8.obj", "small-8.obj", "large-9.obj", "small-9.obj"]

    for i in range(20):
        # Send each file
        send_file(sock, file_names[i])   
        print("Sent: ", file_names[i])

        # Get Ack message from client
        data = sock.recv(1024).decode()
        print("Ack: ", data)
        

    # Close the socket
    sock.close()
       
    
if __name__ == "__main__":
    # Send 20 objects 30 times
    for i in range(2):
        print(f"No. {i} \n")
        send_tcp(i)
        time.sleep(0.1)
