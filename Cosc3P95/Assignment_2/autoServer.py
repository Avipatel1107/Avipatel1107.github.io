import socket
import threading
import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor,SimpleSpanProcessor,ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased

# set up alwaysOn sampler for the server 
alwaysOn_sampler = TraceIdRatioBased(1)

# set the sampler onto the global tracer provider
trace.set_tracer_provider(TracerProvider(sampler=alwaysOn_sampler))
tracer = trace.get_tracer(__name__)

# Use Jaeger exporter alongside Console exporter for local testing
jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

# set up an exporter for sampled spans
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

def handle_client(client_socket):
    with tracer.start_as_current_span("handle_client"):

        # Receive the file name from the client
        file_name = client_socket.recv(1024).decode()

        # Specify the server directory where files will be saved
        server_directory = "./Assign_2/Server_files/"
        file_path = os.path.join(server_directory, os.path.basename(file_name))

        # Start a new span for the file handling operation
        with trace.get_tracer(__name__).start_as_current_span("handle_client"):
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
    # Create a tracer for the main function
    tracer = trace.get_tracer(__name__)

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

        # Create a new span to handle the client
        with tracer.start_as_current_span("main"):
            # Create a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    main()
