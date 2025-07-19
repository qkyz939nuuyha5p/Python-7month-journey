# ✅ Mini Project 2: Bulk File Renamer
# 🔖 Title: bulk_renamer.py
# 📄 Description: Rename all .txt files in a folder to a structured format like file_1.txt, file_2.txt, etc.

import os

target_folder = "test_folder"  # Replace with your folder
count = 1

for filename in os.listdir(target_folder):
    if filename.endswith(".txt"):
        src = os.path.join(target_folder, filename)
        new_name = f"file_{count}.txt"
        dst = os.path.join(target_folder, new_name)
        os.rename(src, dst)
        count += 1

print("✅ All .txt files renamed.")
