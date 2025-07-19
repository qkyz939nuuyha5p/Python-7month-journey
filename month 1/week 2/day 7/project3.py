# ✅ Mini Project 3: Python File Finder (Recursive)
# 🔖 Title: file_finder.py
#  📄 Description: Use glob to find all .py files in current folder and subfolders.

import glob

py_files = glob.glob("**/*.py", recursive=True)

print("📂 Found Python files:")
for file in py_files:
    print("→", file)
