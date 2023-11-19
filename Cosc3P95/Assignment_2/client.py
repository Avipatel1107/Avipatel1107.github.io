import socket
import os


def send_file(file_name):

    # Set the server IP address and port
    server_ip = "127.0.0.1"
    server_port = 7777

    # Create a client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client.connect((server_ip, server_port))

    # Send the file name to the server
    client.send(file_name.encode())

    # Receive the file data from the server
    received_data = client.recv(1024)

    while received_data:
        # Write the received data to a new file in the server directory
        with open("./../Assign_2/Server_files/" + os.path.basename(file_name), 'ab') as file:
            file.write(received_data)
        received_data = client.recv(1024)

    # Close the client socket
    client.close()

def main():
    # Specifying the directory containing the files we want to transfer
    client_files_dir = "./../Assign_2/client_files/"

    # Iterate over each file in the directory
    for file_name in os.listdir(client_files_dir):
        file_path = os.path.join(client_files_dir, file_name)

        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Call the send_file function with the file name
            send_file(file_path)

if __name__ == "__main__":
    main()
