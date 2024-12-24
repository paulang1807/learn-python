## File System
### Traversal
```python
import os
# Get current working directory
path = os.getcwd()

# List contents of the current directory
os.listdir(path)

# Check if a subdirectory exist in a given directory
if os.path.exists('.'):
  subpathexists = True

# Go to the parent directory
os.chdir('../')

# List all csv files in current directory and all subdirectories
dirpath = 'path to traverse'
for (dir_path, dir_names, file_names) in os.walk(dirpath):
    for file in file_names:
        if file.lower().endswith('.csv'):
            print(os.path.join(dir_path, file))
```

### Copy and Move
```python
import shutil  # Shell Utility
# Copy directory from one location to another
# If the destination dir exists and dirs_exist_ok is set to False (which is the default), an error is raised
shutil.copytree("<src path>", "<destination path>", dirs_exist_ok=True)

# Move file
shutil.move("<src path>/<filename>", "<destination path>")
```

### Deletions
```python
# Delete a file at the given path 
os.unlink(path) 

# Delete a folder (must be empty) at the given path
os.rmdir(path) 
```
#### send2trash
- Can be used to send file to trash
- Better than the `shutil.rmtree(path)` alternative 
    - Files deleted using this cannot be recovered
```python
import send2trash
send2trash.send2trash('file_to_delete')
```

## Compression
```python
# Zipping a single file
import zipfile
# Create a zip file
zipped_file_name = zipfile.ZipFile('zip_file.zip','w')
# Add files to the zip file
zipped_file_name.write("file_to_zip.txt",compress_type=zipfile.ZIP_DEFLATED)
zipped_file_name.close()

# Extracting zip file contents
zipped_obj = zipfile.ZipFile('zip_file.zip','r')
zipped_obj.extractall("unzipped_folder_name")
```
```python
# Zipping a folder
import shutil
# compresses the content folder_to_zip to a file called zip_file_name.zip
shutil.make_archive(zip_file_name,'zip',folder_to_zip)  

# Extracting the zipped folder
shutil.unpack_archive(zipped_file_name,folder_name_to_extract_to,'zip')
```

## File Read and Write
### csv reader & writer
```python
import csv

# Reading files
data = open('file.csv',encoding="utf-8")
csv_data = csv.reader(data,delimiter=',')
data_lines = list(csv_data)    
# this is a list of lists
# each row of csv is represented as a list

# Write to new file
output_file = open('new_file.csv','w',newline='')
csv_writer = csv.writer(output_file,delimiter=',')
# write a single line
csv_writer.writerow(['val1','val2','val3'])
# write multiple rows
csv_writer.writerows([['val1','val2','val3'],['val4','val5','val6']])
output_file.close()

# append to existing file
curr_file = open('existing_file.csv','a',newline='')
csv_writer = csv.writer(curr_file)
csv_writer.writerow(['val1','val2','val3'])
curr_file.close()
```