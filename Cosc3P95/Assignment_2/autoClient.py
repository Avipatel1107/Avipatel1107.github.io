import socket
import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor,SimpleSpanProcessor,ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
from opentelemetry.sdk.resources import Resource


# set up Probability (40%) sampler for the client
probability_sampler = TraceIdRatioBased(0.4)

# set the sampler onto the global tracer provider
trace.set_tracer_provider(TracerProvider(sampler=probability_sampler))
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

def receive_file(file_name):
    with tracer.start_as_current_span("send_file"):

    # Set the server IP address and port
        server_ip = "127.0.0.1"
        server_port = 7777

        # Create a client socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client.connect((server_ip, server_port))

        # Send the file name to the server
        client.send(file_name.encode())

        # Specify the directory where you want to save the files
        client_output_dir = "./../Assign_2/Server_files/"

        # Create the directory if it doesn't exist
        os.makedirs(client_output_dir, exist_ok=True)

        # Create the full path for the output file
        output_file_path = os.path.join(client_output_dir, os.path.basename(file_name))

        # Receive the file data from the server
        received_data = client.recv(1024)

    with open(output_file_path, 'wb') as file:
        while received_data:
            # Write the received data to a new file in the client directory
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
            # Call the receive_file function with the file name
            receive_file(file_name)

if __name__ == "__main__":
    main()
