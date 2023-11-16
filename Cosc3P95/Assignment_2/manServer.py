import socket
import threading
import os

def handle_client(client_socket):
    # Receive the file name from the client
    file_name = client_socket.recv(1024).decode()

    # Specify the server directory where files will be saved
    server_directory = "./Assign_2/Server_files/"
    file_path = os.path.join(server_directory, os.path.basename(file_name))

    # Check if the file exists
    if os.path.isfile(file_path):
        # Open and read the file in binary mode
        with open(file_path, 'rb') as file:
            # Read the file contents
            file_data = file.read(1024)
            while file_data:
                # Send the file data to the client
                client_socket.send(file_data)
                file_data = file.read(1024)
    else:
        # If the file does not exist, send an error message
        client_socket.send("File not found".encode())

    # Close the client socket
    client_socket.close()

def main():
    # Set the server IP address and port
    server_ip = "127.0.0.1"
    server_port = 7777

    # Create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)

    print(f"[*] Listening on {server_ip}:{server_port}")

    while True:
        # Accept a client connection
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
