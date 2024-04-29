import os
import zipfile
import json
from datetime import datetime

def zip_and_delete_files(source_dir, output_dir, batch_size):
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    all_files = [os.path.join(foldername, filename) for foldername, _, filenames in os.walk(source_dir) for filename in filenames]
    file_batches = [all_files[i:i + batch_size] for i in range(0, len(all_files), batch_size)]
    log_filename = f"log_{current_datetime}.json"
    log_path = os.path.join(output_dir, log_filename)
    
    log_data = {"batches": []}
    
    for idx, file_batch in enumerate(file_batches):
        batch_data = {"files": []}
        for file_path in file_batch:
            creation_time = os.path.getctime(file_path)
            creation_datetime = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d %H:%M:%S")
            batch_data["files"].append({
                "name": os.path.basename(file_path),
                "created_at": creation_datetime,
                "compressed_at": None,
                "removed_at": None
            })
        
        zip_filename = f"batch_{idx + 1}.zip"
        zip_path = os.path.join(output_dir, zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for file_path in file_batch:
                arcname = os.path.relpath(file_path, source_dir)
                zip_file.write(file_path, arcname)
                for file_entry in batch_data["files"]:
                    if file_entry["name"] == os.path.basename(file_path):
                        file_entry["compressed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        break
        
        log_data["batches"].append({
            "batch_number": idx + 1,
            "zip_filename": zip_filename,
            "log_data": batch_data
        })
        
        for file_path in file_batch:
            os.remove(file_path)
            
            for file_entry in batch_data["files"]:
                if file_entry["name"] == os.path.basename(file_path):
                    file_entry["removed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    break
            
            print(f"Deleted file: '{file_path}'.")
    
    with open(log_path, 'w') as log_file:
        json.dump(log_data, log_file, indent=2)
    
    print(f"Log file created successfully at '{log_path}'.")

source_directory = '/home/navid/Desktop/zipper/files'
output_directory = '/home/navid/Desktop/zipper/zipes'
batch_size = 20

zip_and_delete_files(source_directory, output_directory, batch_size)
