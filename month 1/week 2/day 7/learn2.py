# Deleting Files and Directories:
'''
You can delete single files, directories, and entire directory trees using the methods found in the os, shutil, and pathlib modules. The following sections describe how to delete files and directories that you no longer need.

Deleting Files in Python
To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink().

os.remove() and os.unlink() are semantically identical. To delete a file using os.remove(), do the following:

import os

data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
os.remove(data_file)
Deleting a file using os.unlink() is similar to how you do it using os.remove():

import os

data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
os.unlink(data_file)
Calling .unlink() or .remove() on a file deletes the file from the filesystem. These two functions will throw an OSError if the path passed to them points to a directory instead of a file. To avoid this, you can either check that what you’re trying to delete is actually a file and only delete it if it is, or you can use exception handling to handle the OSError:

import os

data_file = 'home/data.txt'

# If the file exists, delete it
if os.path.isfile(data_file):
    os.remove(data_file)
else:
    print(f'Error: {data_file} not a valid filename')
os.path.isfile() checks whether data_file is actually a file. If it is, it is deleted by the call to os.remove(). If data_file points to a folder, an error message is printed to the console.

The following example shows how to use exception handling to handle errors when deleting files:

import os

data_file = 'home/data.txt'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}')
The code above attempts to delete the file first before checking its type. If data_file isn’t actually a file, the OSError that is thrown is handled in the except clause, and an error message is printed to the console. The error message that gets printed out is formatted using Python f-strings.

Finally, you can also use pathlib.Path.unlink() to delete files:

from pathlib import Path

data_file = Path('home/data.txt')

try:
    data_file.unlink()
except IsADirectoryError as e:
    print(f'Error: {data_file} : {e.strerror}')
This creates a Path object called data_file that points to a file. Calling .remove() on data_file will delete home/data.txt. If data_file points to a directory, an IsADirectoryError is raised. It is worth noting that the Python program above has the same permissions as the user running it. If the user does not have permission to delete the file, a PermissionError is raised.

Deleting Directories
The standard library offers the following functions for deleting directories:

os.rmdir()
pathlib.Path.rmdir()
shutil.rmtree()
To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the directory you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. Here is how to delete a folder:

import os

trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
Here, the trash_dir directory is deleted by passing its path to os.rmdir(). If the directory isn’t empty, an error message is printed to the screen:

Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
OSError: [Errno 39] Directory not empty: 'my_documents/bad_dir'
Alternatively, you can use pathlib to delete directories:

from pathlib import Path

trash_dir = Path('my_documents/bad_dir')

try:
    trash_dir.rmdir()
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
Here, you create a Path object that points to the directory to be deleted. Calling .rmdir() on the Path object will delete it if it is empty.Deleting Entire Directory Trees
To delete non-empty directories and entire directory trees, Python offers shutil.rmtree():

import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')
Everything in trash_dir is deleted when shutil.rmtree() is called on it. There may be cases where you want to delete empty folders recursively. You can do this using one of the methods discussed above in conjunction with os.walk():

import os

for dirpath, dirnames, files in os.walk('.', topdown=False):
    try:
        os.rmdir(dirpath)
    except OSError as ex:
        pass
This walks down the directory tree and tries to delete each directory it finds. If the directory isn’t empty, an OSError is raised and that directory is skipped. The table below lists the functions covered in this section:

Function	Description
os.remove()	Deletes a file and does not delete directories
os.unlink()	Is identical to os.remove() and deletes a single file
pathlib.Path.unlink()	Deletes a file and cannot delete directories
os.rmdir()	Deletes an empty directory
pathlib.Path.rmdir()	Deletes an empty directory
shutil.rmtree()	Deletes entire directory tree and can be used to delete non-empty directories'''

# Copying, Moving, and Renaming Files and Directories:
'''
Python ships with the shutil module. shutil is short for shell utilities. It provides a number of high-level operations on files to support copying, archiving, and removal of files and directories. In this section, you’ll learn how to move and copy files and directories.

Copying Files in Python
shutil offers a couple of functions for copying files. The most commonly used functions are shutil.copy() and shutil.copy2(). To copy a file from one location to another using shutil.copy(), do the following:

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy(src, dst)
shutil.copy() is comparable to the cp command in UNIX based systems. shutil.copy(src, dst) will copy the file src to the location specified in dst. If dst is a file, the contents of that file are replaced with the contents of src. If dst is a directory, then src will be copied into that directory. shutil.copy() only copies the file’s contents and the file’s permissions. Other metadata like the file’s creation and modification times are not preserved.

To preserve all file metadata when copying, use shutil.copy2():

import shutil

src = 'path/to/file.txt'
dst = 'path/to/dest_dir'
shutil.copy2(src, dst)
Using .copy2() preserves details about the file such as last access time, permission bits, last modification time, and flags.

Copying Directories
While shutil.copy() only copies a single file, shutil.copytree() will copy an entire directory and everything contained in it. shutil.copytree(src, dest) takes two arguments: a source directory and the destination directory where files and folders will be copied to.

Here’s an example of how to copy the contents of one folder to a different location:

>>> import shutil
>>> shutil.copytree('data_1', 'data1_backup')
'data1_backup'
In this example, .copytree() copies the contents of data_1 to a new location data1_backup and returns the destination directory. The destination directory must not already exist. It will be created as well as missing parent directories. shutil.copytree() is a good way to back up your files.

Moving Files and Directories
To move a file or directory to another location, use shutil.move(src, dst).

src is the file or directory to be moved and dst is the destination:

>>> import shutil
>>> shutil.move('dir_1/', 'backup/')
'backup'
shutil.move('dir_1/', 'backup/') moves dir_1/ into backup/ if backup/ exists. If backup/ does not exist, dir_1/ will be renamed to backup.

Renaming Files and Directories
Python includes os.rename(src, dst) for renaming files and directories:

>>> os.rename('first.zip', 'first_01.zip')
The line above will rename first.zip to first_01.zip. If the destination path points to a directory, it will raise an OSError.

Another way to rename files or directories is to use rename() from the pathlib module:

>>> from pathlib import Path
>>> data_file = Path('data_01.txt')
>>> data_file.rename('data.txt')
To rename files using pathlib, you first create a pathlib.Path() object that contains a path to the file you want to replace. The next step is to call rename() on the path object and pass a new filename for the file or directory you’re renaming.
'''