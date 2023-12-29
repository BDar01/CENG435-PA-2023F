import socket
import os

HOST = "172.17.0.2"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def send_file(file_path, connection):
    with open(file_path, 'rb') as file:
        file_size = os.path.getsize(file_path)

        # Send file size as a fixed-width string (e.g., 10 characters)
        connection.sendall(str(file_size).ljust(10).encode())

        data = file.read(1024)
        while data:
            connection.send(data)
            data = file.read(1024)

        print(f"File '{file_path}' sent successfully")

def send_files():
    server_ip = '127.0.0.1'
    server_port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        file_paths = ['../../objects/large-0.obj', '../../objects/small-0.obj']

        for file_path in file_paths:
            send_file(file_path, s)

if __name__ == "__main__":
    send_files()
