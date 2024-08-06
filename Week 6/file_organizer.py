import os
import shutil
import sys

def split_extension(directory1):
    filename, extension = os.path.splitext(directory1)
    return extension.lower()[1:]

def categorize_by_extension(directory):
    category_folders = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            extension = split_extension(filepath)
        
            if extension:
                category_folder = os.path.join(directory, f"{extension}_files")
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                category_folders[extension] = category_folder
            if extension:
                shutil.move(filepath, category_folders[extension])

def main_file_organizer(directory):
    try:
        categorize_by_extension(directory)
        print(f"Folders created and files moved with 'extension_file' format in '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_organizer.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        main_file_organizer(directory_path)