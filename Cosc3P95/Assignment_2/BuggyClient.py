import socket
import os
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
import gzip
import logging 
import random
import time
import csv

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

# Function to initialize the CSV file with headers
def initialize_csv():
    with open('execution_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['file_name', 'delay_introduced', 'failure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

# Add this function to log data during each execution
def log_execution_data(file_name, delay_introduced, failure):
    with open('execution_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['file_name', 'delay_introduced', 'failure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Check if the file is empty and write the header if needed
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'file_name': file_name,
            'delay_introduced': delay_introduced,
            'failure': failure,
        })

def receive_file(file_name):
     with tracer.start_as_current_span("send_file"):
        server_ip = "127.0.0.1"
        server_port = 7777

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        failure=False
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
                    logging.info(f"Received data for file: {file_name}")

                        # Introduce a deliberate delay only in some cases
                    if random.random() < 0.9:  # 90% chance of introducing a delay
                        delay_seconds = random.uniform(0.5, 2.0)  # Random delay between 0.5 and 2.0 seconds
                        logging.info(f"Introducing a deliberate delay of {delay_seconds} seconds.")
                        time.sleep(delay_seconds)
                        delay_introduced=True
                        logging.warning("Deliberate delay introduced for testing purposes.")
                    else:
                        delay_introduced=False

                    if not os.path.isfile(output_file_path):
                        failure = True
                        logging.error(f"File not found: {file_name}")
                    
                    log_execution_data(file_name, delay_introduced, failure)

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