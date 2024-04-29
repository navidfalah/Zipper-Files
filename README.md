# Junk File Zipper 🗑️📁

<details>
<summary>Overview ℹ️</summary>

This Python script is designed to zip and delete batches of junk files from a specified directory. Additionally, it creates a log file to keep track of the zipping and deletion process.

</details>

<details>
<summary>Features 🚀</summary>

- Zips junk files in batches.
- Deletes junk files after zipping.
- Generates a detailed log file.

</details>

<details>
<summary>Requirements 🛠️</summary>

- Python 3.x
- `os` module
- `zipfile` module
- `json` module
- `datetime` module

</details>

<details>
<summary>Usage 📝</summary>

1. Set the source directory (`source_directory`) where the junk files are located.
2. Set the output directory (`output_directory`) where the zipped files and log file will be saved.
3. Set the batch size (`batch_size`) to determine the number of files zipped in each batch.
4. Run the script.

</details>

<details>
<summary>Example Usage 🛠️</summary>

```python
source_directory = '/home/navid/Desktop/zipper/files'
output_directory = '/home/navid/Desktop/zipper/zipes'
batch_size = 20

zip_and_delete_files(source_directory, output_directory, batch_size)
</details>
<details>
<summary>Sample Output 📄</summary>
Created junk_file_1.txt with size 1 MB
Created junk_file_2.txt with size 1 MB
...
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_1.txt'.
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_2.txt'.
...
Log file created successfully at '/home/navid/Desktop/zipper/zipes/log_2023-12-22_16-19-06.json'.

Created junk_file_1.txt with size 1 MB
Created junk_file_2.txt with size 1 MB
...
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_1.txt'.
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_2.txt'.
...
Log file created successfully at '/home/navid/Desktop/zipper/zipes/log_2023-12-22_16-19-06.json'.

Sure, here it is:

markdown

# Junk File Zipper 🗑️📁

<details>
<summary>Overview ℹ️</summary>

This Python script is designed to zip and delete batches of junk files from a specified directory. Additionally, it creates a log file to keep track of the zipping and deletion process.

</details>

<details>
<summary>Features 🚀</summary>

- Zips junk files in batches.
- Deletes junk files after zipping.
- Generates a detailed log file.

</details>

<details>
<summary>Requirements 🛠️</summary>

- Python 3.x
- `os` module
- `zipfile` module
- `json` module
- `datetime` module

</details>

<details>
<summary>Usage 📝</summary>

1. Set the source directory (`source_directory`) where the junk files are located.
2. Set the output directory (`output_directory`) where the zipped files and log file will be saved.
3. Set the batch size (`batch_size`) to determine the number of files zipped in each batch.
4. Run the script.

</details>

<details>
<summary>Example Usage 🛠️</summary>

```python
source_directory = '/home/navid/Desktop/zipper/files'
output_directory = '/home/navid/Desktop/zipper/zipes'
batch_size = 20

zip_and_delete_files(source_directory, output_directory, batch_size)

</details>
<details>
<summary>Sample Output 📄</summary>

arduino

Created junk_file_1.txt with size 1 MB
Created junk_file_2.txt with size 1 MB
...
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_1.txt'.
Deleted file: '/home/navid/Desktop/zipper/files/junk_file_2.txt'.
...
Log file created successfully at '/home/navid/Desktop/zipper/zipes/log_2023-12-22_16-19-06.json'.

</details>
<details>
<summary>Log Structure 📋</summary>

The log file (log_<timestamp>.json) contains information about each batch, including the batch number, zip filename, and details of each file within the batch.
"batches": [
    {
        "batch_number": 1,
        "zip_filename": "batch_1.zip",
        "log_data": {
            "files": [
                {
                    "name": "junk_file_1.txt",
                    "created_at": "2023-12-22 16:19:06",
                    "compressed_at": "2023-12-22 16:19:09",
                    "removed_at": "2023-12-22 16:19:09"
                },
                {
                    "name": "junk_file_2.txt",
                    "created_at": "2023-12-22 16:19:06",
                    "compressed_at": "2023-12-22 16:19:09",
                    "removed_at": "2023-12-22 16:19:09"
                },
                ...
            ]
        }
    },
    ...
]

</details>
<details>
<summary>Additional Functionality 🌟</summary>

The script also includes a function to create junk files of specified size for testing purposes.
</details>
<details>
