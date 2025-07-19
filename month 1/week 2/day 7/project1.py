#✅ Mini Project 1: Auto File Organizer:
# 🔖 Title: file_organizer.py
# 📄 Description: Automatically organize files by their extension into folders.

import os
import shutil

source_folder = "test_folder"  # Replace with your target folder path
file_types = {
    ".txt": "TextFiles",
    ".jpg": "Images",
    ".pdf": "PDFs",
    ".py": "PythonFiles"
}

# Create folders if not exist
for folder in file_types.values():
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

# Move files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        if ext in file_types:
            shutil.move(file_path, os.path.join(source_folder, file_types[ext], file))

print("✅ Files organized by type.")
