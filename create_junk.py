import os

def create_junk_file(file_path, size_mb):
    with open(file_path, 'wb') as file:
        # Set the file size to 1 MB
        file.write(b'\0' * (size_mb * 1024 * 1024))

def main():
    desktop_directory = 'files'  # Change this to your desktop path
    
    if not os.path.exists(desktop_directory):
        os.makedirs(desktop_directory)

    num_files = 400

    file_size_mb = 1

    for i in range(1, num_files + 1):
        file_name = f'junk_file_{i}.txt'
        file_path = os.path.join(desktop_directory, file_name)
        create_junk_file(file_path, file_size_mb)
        print(f'Created {file_name} with size {file_size_mb} MB')

if __name__ == "__main__":
    main()
