import socket
import threading
import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
import gzip
import logging

# Feature Flags
ENABLE_COMPRESSION = True
ENABLE_CHUNKING_STREAMING = True

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

# Rate Limiting Parameters
RATE_LIMIT = 5  # Maximum number of connections allowed per second
rate_limit_lock = threading.Lock()

def handle_client(client_socket):
    with tracer.start_as_current_span("handle_client"):
        file_name = client_socket.recv(1024).decode()

        try:
            server_directory = "./Assign_2/Server_files/"
            file_path = os.path.join(server_directory, os.path.basename(file_name))

            with trace.get_tracer(__name__).start_as_current_span("handle_client"):
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as file:
                        while True:
                            file_data = file.read(1024)
                            if not file_data:
                                break
                            if ENABLE_COMPRESSION:
                                compressed_data = gzip.compress(file_data)
                            else:
                                compressed_data = file_data
                            if ENABLE_CHUNKING_STREAMING:
                                client_socket.sendall(compressed_data)
                            else:
                                client_socket.sendall(file_data)

                            logging.info(f"Sent data for file: {file_name}")

                else:
                    client_socket.send("File not found".encode())
                    

        finally:
            client_socket.close()

def rate_limited_accept(server):
    with rate_limit_lock:
        return server.accept()

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
        # Accept a client connection with rate limiting
        client_socket, addr = rate_limited_accept(server)

        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        # Create a new span to handle the client
        with tracer.start_as_current_span("main"):
            # Create a new thread to handle the client
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    main()