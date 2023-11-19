import os
import random


# Specify the local folder path where you want to create the files.
folder_path = "./../Assign_2/client_files"

# Function to create a random file of a specified size
def create_random_file(file_path, size_bytes):
    with open(file_path, 'wb') as file:
        file.write(os.urandom(size_bytes))

# Create at least 20 random files with varying sizes
for i in range(1, 21):
    # Generate a random size between 5KB and 100MB
    size_bytes = random.randint(5 * 1024, 100 * 1024 * 1024)
    file_name = f"file_{i}.txt"
    file_path = os.path.join(folder_path, file_name)
    create_random_file(file_path, size_bytes)
    print(f"Created {file_name} with size {size_bytes / 1024} KB")

print("Files created successfully.")
