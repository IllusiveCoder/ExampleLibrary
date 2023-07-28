import os
import shutil

'''Build a file organizer script that helps users 
organize files in a specific directory based on their 
file types. The script will scan the target directory, 
identify the file types, and move them into designated 
subdirectories (e.g., "Images," "Documents," "Videos," 
etc.).'''

class FileOrganizer:
    def __init__(self, target_directory):
        self.target_directory = target_directory

    def organize_files(self):
        file_types = {}
        for filename in os.listdir(self.target_directory):
            if os.path.isfile(os.path.join(self.target_directory, filename)):
                file_extension = os.path.splitext(filename)[1].lower()
                file_type = file_extension[1:] if file_extension else "Others"
                if file_type not in file_types:
                    file_types[file_type] = []
                file_types[file_type].append(filename)

        for file_type, files in file_types.items():
            type_directory = os.path.join(self.target_directory, file_type.capitalize())
            os.makedirs(type_directory, exist_ok=True)
            for file in files:
                src_path = os.path.join(self.target_directory, file)
                dst_path = os.path.join(type_directory, file)
                shutil.move(src_path, dst_path)

# Usage example
target_directory = "C:/Users/username/Downloads"
file_organizer = FileOrganizer(target_directory)
file_organizer.organize_files()