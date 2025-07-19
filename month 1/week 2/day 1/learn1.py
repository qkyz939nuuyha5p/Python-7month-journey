#Python Functions
'''
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

built-in functions
user-defined functions
1. built-in functions:
These functions are defined and pre-coded in Python. Some examples of built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

2. user-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax:

def function_name(parameters):
    Code and Statements

Create a function using the def keyword, followed by a function name, followed by parentheses () and a colon :.
Any parameters and arguments should be placed within the parentheses.
Rules for naming functions are similar to those for naming variables.
Any statements and other code within the function should be indented.
Call a function:
We call a function by giving the function name, followed by parameters (if any) in the parentheses.'''
#e.g
def name(fname,lname):
    print("hello",fname,lname)
name("parikshan","shahi")