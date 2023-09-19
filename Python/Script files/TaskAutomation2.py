import os
import shutil

'''Description: This script automates common computer tasks. 
It can perform tasks like file organization, data backup, or 
repetitive data processing. Users can customize the tasks by 
editing the script and adding their own functions.'''

# Function to organize files into folders based on file extension
def organize_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1]
            folder_path = os.path.join(destination_folder, file_extension[1:])
            os.makedirs(folder_path, exist_ok=True)
            destination_path = os.path.join(folder_path, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {folder_path}")

# Function to backup files to a specified location
def backup_files(source_folder, backup_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_folder)
            backup_path = os.path.join(backup_folder, relative_path)
            os.makedirs(os.path.dirname(backup_path), exist_ok=True)
            shutil.copy2(source_path, backup_path)
            print(f"Backed up {file} to {backup_path}")

# Usage example
source_folder = "source_directory"
destination_folder = "organized_files"
backup_folder = "backup_directory"

organize_files(source_folder, destination_folder)
backup_files(source_folder, backup_folder)
