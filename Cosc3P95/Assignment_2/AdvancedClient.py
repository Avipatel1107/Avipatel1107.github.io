import socket
import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
import gzip

# Feature Flags
ENABLE_COMPRESSION = True
ENABLE_CHUNKING_STREAMING = True

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
        server_ip = "127.0.0.1"
        server_port = 7777

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((server_ip, server_port))
            client.send(file_name.encode())

            client_output_dir = "./../Assign_2/Server_files/"
            os.makedirs(client_output_dir, exist_ok=True)
            output_file_path = os.path.join(client_output_dir, os.path.basename(file_name))

            with open(output_file_path, 'wb') as file:
                while True:
                    received_data = client.recv(1024)
                    if not received_data:
                        break
                    if ENABLE_COMPRESSION:
                        try:
                            decompressed_data = gzip.decompress(received_data)
                        except gzip.BadGzipFile:
                            decompressed_data=received_data
                    else:
                        decompressed_data = received_data
                    file.write(decompressed_data)

        finally:
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
