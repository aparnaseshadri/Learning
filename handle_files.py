input_file_path = 'input_file.txt'
output_file_path = 'output_file.txt'
chunk_size = 1024  # Size of each chunk in bytes

with open(input_file_path, 'r') as input_file:
    with open(output_file_path, 'w') as output_file:
        while True:
            chunk = input_file.read(chunk_size)
            if not chunk:
                break
            output_file.write(chunk)

print(f"Content from {input_file_path} has been written to {output_file_path}.")
