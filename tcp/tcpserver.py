import socket
import hashlib

HOST = ""  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def receive_file(connection):
    # Receive fixed-width string (e.g., 10 characters) for file size
    file_size_str = connection.recv(10).decode().rstrip()

    # Extract numeric characters from the received string
    file_size_digits = ''.join(filter(str.isdigit, file_size_str))

    try:
        file_size = int(file_size_digits)
    except ValueError:
        print(f"Invalid file size: {file_size_str}")
        return

    received_data = b""
    while len(received_data) < file_size:
        data = connection.recv(1024)
        if not data:
            break
        received_data += data

    # Generate a unique filename
    unique_filename = f'received_file_{hashlib.md5(received_data).hexdigest()}.obj'

    with open(unique_filename, 'wb') as file:
        file.write(received_data)

    print(f"File '{unique_filename}' received. Size: {file_size} bytes")

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = s.accept()

        with conn:
            print(f"Connection from {addr}")

            # Receive multiple files
            for _ in range(2):  # Assuming 2 files are being sent
                receive_file(conn)
