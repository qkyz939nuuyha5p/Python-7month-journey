# Getting a Directory Listing:
'''
Suppose your current working directory has a subdirectory called my_directory that has the following contents:

my_directory/
|
├── sub_dir/
|   ├── bar.py
|   └── foo.py
|
├── sub_dir_b/
|   └── file4.txt
|
├── sub_dir_c/
|   ├── config.py
|   └── file5.txt
|
├── file1.py
├── file2.csv
└── file3.txt
The built-in os module has a number of useful functions that can be used to list directory contents and filter the results. To get a list of all the files and folders in a particular directory in the filesystem, use os.listdir() in legacy versions of Python or os.scandir() in Python 3. os.scandir() is the preferred method to use if you also want to get file and directory properties such as file size and modification date.

Directory Listing in Legacy Python Versions
In versions of Python prior to Python 3, os.listdir() is the method to use to get a directory listing:

>>> import os
>>> entries = os.listdir('my_directory/')
os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given by the path argument:

>>> os.listdir('my_directory/')
['sub_dir_c', 'file1.py', 'sub_dir_b', 'file3.txt', 'file2.csv', 'sub_dir']
A directory listing like that isn’t easy to read. Printing out the output of a call to os.listdir() using a loop helps clean things up:

>>> entries = os.listdir('my_directory/')
>>> for entry in entries:
...     print(entry)
...
...
sub_dir_c
file1.py
sub_dir_b
file3.txt
file2.csv
sub_dir
Directory Listing in Modern Python Versions
In modern versions of Python, an alternative to os.listdir() is to use os.scandir() and pathlib.Path().

os.scandir() was introduced in Python 3.5 and is documented in PEP 471. os.scandir() returns an iterator as opposed to a list when called:

>>> import os
>>> entries = os.scandir('my_directory/')
>>> entries
<posix.ScandirIterator object at 0x7f5b047f3690>
The ScandirIterator points to all the entries in the current directory. You can loop over the contents of the iterator and print out the filenames:

import os

with os.scandir('my_directory/') as entries:
    for entry in entries:
        print(entry.name)
Here, os.scandir() is used in conjunction with the with statement because it supports the context manager protocol. Using a context manager closes the iterator and frees up acquired resources automatically after the iterator has been exhausted. The result is a print out of the filenames in my_directory/ just like you saw in the os.listdir() example:

sub_dir_c
file1.py
sub_dir_b
file3.txt
file2.csv
sub_dir
Another way to get a directory listing is to use the pathlib module:

from pathlib import Path

entries = Path('my_directory/')
for entry in entries.iterdir():
    print(entry.name)
The objects returned by Path are either PosixPath or WindowsPath objects depending on the OS.

pathlib.Path() objects have an .iterdir() method for creating an iterator of all files and folders in a directory. Each entry yielded by .iterdir() contains information about the file or directory such as its name and file attributes. pathlib was first introduced in Python 3.4 and is a great addition to Python that provides an object oriented interface to the filesystem.

In the example above, you call pathlib.Path() and pass a path argument to it. Next is the call to .iterdir() to get a list of all files and directories in my_directory.

pathlib offers a set of classes featuring most of the common operations on paths in an easy, object-oriented way. Using pathlib is more if not equally efficient as using the functions in os. Another benefit of using pathlib over os is that it reduces the number of imports you need to make to manipulate filesystem paths. For more information, read Python’s pathlib Module: Taming the File System.

Note: To get started with pathlib, check out Python Basics: File System Operations and the associated exercises.

Running the code above produces the following:

sub_dir_c
file1.py
sub_dir_b
file3.txt
file2.csv
sub_dir
Using pathlib.Path() or os.scandir() instead of os.listdir() is the preferred way of getting a directory listing, especially when you’re working with code that needs the file type and file attribute information. pathlib.Path() offers much of the file and path handling functionality found in os and shutil, and it’s methods are more efficient than some found in these modules. We will discuss how to get file properties shortly.

Here are the directory-listing functions again:

Function	Description
os.listdir()	Returns a list of all files and folders in a directory
os.scandir()	Returns an iterator of all the objects in a directory including file attribute information
pathlib.Path.iterdir()	Returns an iterator of all the objects in a directory including file attribute information
These functions return a list of everything in the directory, including subdirectories. This might not always be the behavior you want. The next section will show you how to filter the results from a directory listing.

Listing All Files in a Directory
This section will show you how to print out the names of files in a directory using os.listdir(), os.scandir(), and pathlib.Path(). To filter out directories and only list files from a directory listing produced by os.listdir(), use os.path:

import os

# List all files in a directory using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)
Here, the call to os.listdir() returns a list of everything in the specified path, and then that list is filtered by os.path.isfile() to only print out files and not directories. This produces the following output:

file1.py
file3.txt
file2.csv
An easier way to list files in a directory is to use os.scandir() or pathlib.Path():

import os

# List all files in a directory using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
Using os.scandir() has the advantage of looking cleaner and being easier to understand than using os.listdir(), even though it is one line of code longer. Calling entry.is_file() on each item in the ScandirIterator returns True if the object is a file. Printing out the names of all files in the directory gives you the following output:

file1.py
file3.txt
file2.csv
Here’s how to list files in a directory using pathlib.Path():

from pathlib import Path

basepath = Path('my_directory/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)
Here, you call .is_file() on each entry yielded by .iterdir(). The output produced is the same:

file1.py
file3.txt
file2.csv
The code above can be made more concise if you combine the for loop and the if statement into a single generator expression. Dan Bader has an excellent article on generator expressions and list comprehensions.

The modified version looks like this:

from pathlib import Path

# List all files in directory using pathlib
basepath = Path('my_directory/')
files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
for item in files_in_basepath:
    print(item.name)
This produces exactly the same output as the example before it. This section showed that filtering files or directories using os.scandir() and pathlib.Path() feels more intuitive and looks cleaner than using os.listdir() in conjunction with os.path.

Listing Subdirectories
To list subdirectories instead of files, use one of the methods below. Here’s how to use os.listdir() and os.path():

import os

# List all subdirectories using os.listdir
basepath = 'my_directory/'
for entry in os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)
Manipulating filesystem paths this way can quickly become cumbersome when you have multiple calls to os.path.join(). Running this on my computer produces the following output:

sub_dir_c
sub_dir_b
sub_dir
Here’s how to use os.scandir():

import os

# List all subdirectories using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
As in the file listing example, here you call .is_dir() on each entry returned by os.scandir(). If the entry is a directory, .is_dir() returns True, and the directory’s name is printed out. The output is the same as above:

sub_dir_c
sub_dir_b
sub_dir
Here’s how to use pathlib.Path():

from pathlib import Path

# List all subdirectory using pathlib
basepath = Path('my_directory/')
for entry in basepath.iterdir():
    if entry.is_dir():
        print(entry.name)
Calling .is_dir() on each entry of the basepath iterator checks if an entry is a file or a directory. If the entry is a directory, its name is printed out to the screen, and the output produced is the same as the one from the previous example:

sub_dir_c
sub_dir_b
sub_dir'''

# Making Directories:
'''Sooner or later, the programs you write will have to create directories in order to store data in them. os and pathlib include functions for creating directories. We’ll consider these:

Function	Description
os.mkdir()	Creates a single subdirectory
pathlib.Path.mkdir()	Creates single or multiple directories
os.makedirs()	Creates multiple directories, including intermediate directories
Creating a Single Directory
To create a single directory, pass a path to the directory as a parameter to os.mkdir():

import os

os.mkdir('example_directory/')
If a directory already exists, os.mkdir() raises FileExistsError. Alternatively, you can create a directory using pathlib:

from pathlib import Path

p = Path('example_directory/')
p.mkdir()
If the path already exists, mkdir() raises a FileExistsError:

>>> p.mkdir()
Traceback (most recent call last):
  File '<stdin>', line 1, in <module>
  File '/usr/lib/python3.5/pathlib.py', line 1214, in mkdir
    self._accessor.mkdir(self, mode)
  File '/usr/lib/python3.5/pathlib.py', line 371, in wrapped
    return strfunc(str(pathobj), *args)
FileExistsError: [Errno 17] File exists: '.'
[Errno 17] File exists: '.'
To avoid errors like this, catch the error when it happens and let your user know:

from pathlib import Path

p = Path('example_directory')
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)
Alternatively, you can ignore the FileExistsError by passing the exist_ok=True argument to .mkdir():

from pathlib import Path

p = Path('example_directory')
p.mkdir(exist_ok=True)
This will not raise an error if the directory already exists.Creating Multiple Directories
os.makedirs() is similar to os.mkdir(). The difference between the two is that not only can os.makedirs() create individual directories, it can also be used to create directory trees. In other words, it can create any necessary intermediate folders in order to ensure a full path exists.

os.makedirs() is similar to running mkdir -p in Bash. For example, to create a group of directories like 2018/10/05, all you have to do is the following:

import os


os.makedirs('2018/10/05')
This will create a nested directory structure that contains the folders 2018, 10, and 05:

.
|
└── 2018/
    └── 10/
        └── 05/
.makedirs() creates directories with default permissions. If you need to create directories with different permissions call .makedirs() and pass in the mode you would like the directories to be created in:

import os

os.makedirs('2018/10/05', mode=0o770)
This creates the 2018/10/05 directory structure and gives the owner and group users read, write, and execute permissions. The default mode is 0o777, and the file permission bits of existing parent directories are not changed. For more details on file permissions, and how the mode is applied, see the docs.

Run tree to confirm that the right permissions were applied:

$ tree -p -i .
.
[drwxrwx---]  2018
[drwxrwx---]  10
[drwxrwx---]  05
This prints out a directory tree of the current directory. tree is normally used to list contents of directories in a tree-like format. Passing the -p and -i arguments to it prints out the directory names and their file permission information in a vertical list. -p prints out the file permissions, and -i makes tree produce a vertical list without indentation lines.

As you can see, all of the directories have 770 permissions. An alternative way to create directories is to use .mkdir() from pathlib.Path:

import pathlib

p = pathlib.Path('2018/10/05')
p.mkdir(parents=True)
Passing parents=True to Path.mkdir() makes it create the directory 05 and any parent directories necessary to make the path valid.

By default, os.makedirs() and Path.mkdir() raise an OSError if the target directory already exists. This behavior can be overridden (as of Python 3.2) by passing exist_ok=True as a keyword argument when calling each function.

Running the code above produces a directory structure like the one below in one go:

.
|
└── 2018/
    └── 10/
        └── 05/
I prefer using pathlib when creating directories because I can use the same function to create single or nested directories.'''

#Filename Pattern Matching Using glob:
'''
Another useful module for pattern matching is glob.

.glob() in the glob module works just like fnmatch.fnmatch(), but unlike fnmatch.fnmatch(), it treats files beginning with a period (.) as special.

UNIX and related systems translate name patterns with wildcards like ? and * into a list of files. This is called globbing.

For example, typing mv *.py python_files/ in a UNIX shell moves (mv) all files with the .py extension from the current directory to the directory python_files. The * character is a wildcard that means “any number of characters,” and *.py is the glob pattern. This shell capability is not available in the Windows Operating System. The glob module adds this capability in Python, which enables Windows programs to use this feature.

Here’s an example of how to use glob to search for all Python (.py) source files in the current directory:

>>> import glob
>>> glob.glob('*.py')
['admin.py', 'tests.py']
glob.glob('*.py') searches for all files that have the .py extension in the current directory and returns them as a list. glob also supports shell-style wildcards to match patterns:

>>> import glob
>>> for name in glob.glob('*[0-9]*.txt'):
...     print(name)
This finds all text (.txt) files that contain digits in the filename:

data_01.txt
data_03.txt
data_03_backup.txt
data_02_backup.txt
data_02.txt
data_01_backup.txt
glob makes it easy to search for files recursively in subdirectories too:

>>> import glob
>>> for file in glob.iglob('**/*.py', recursive=True):
...     print(file)
This example makes use of glob.iglob() to search for .py files in the current directory and subdirectories. Passing recursive=True as an argument to .iglob() makes it search for .py files in the current directory and any subdirectories. The difference between glob.iglob() and glob.glob() is that .iglob() returns an iterator instead of a list.

Running the program above produces the following:

admin.py
tests.py
sub_dir/file1.py
sub_dir/file2.py
pathlib contains similar methods for making flexible file listings. The example below shows how you can use .Path.glob() to list file types that start with the letter p:

>>> from pathlib import Path
>>> p = Path('.')
>>> for name in p.glob('*.p*'):
...     print(name)

admin.py
scraper.py
docs.pdf
Calling p.glob('*.p*') returns a generator object that points to all files in the current directory that start with the letter p in their file extension.

Path.glob() is similar to os.glob() discussed above. As you can see, pathlib combines many of the best features of the os, os.path, and glob modules into one single module, which makes it a joy to use.

To recap, here is a table of the functions we have covered in this section:

Function	Description
startswith()	Tests if a string starts with a specified pattern and returns True or False
endswith()	Tests if a string ends with a specified pattern and returns True or False
fnmatch.fnmatch(filename, pattern)	Tests whether the filename matches the pattern and returns True or False
glob.glob()	Returns a list of filenames that match a pattern
pathlib.Path.glob()	Finds patterns in path names and returns a generator object'''
