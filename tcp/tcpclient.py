import socket
import os

def send_file():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    file_path = os.path.join(os.path.dirname(__file__), '..', 'objects', 'small-0.obj')  # Update the file path
    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    print(f"File '{file_path}' sent successfully")

    client_socket.close()

if __name__ == "__main__":
    send_file()
