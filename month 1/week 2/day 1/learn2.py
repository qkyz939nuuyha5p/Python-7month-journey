#Function Arguments
'''
There are four types of arguments that we can provide in a function:

Default Arguments
Keyword Arguments
Required Arguments
Variable-length Arguments
'''
#Default arguments:
'''
We can provide a default value while creating a function. This way the function assumes
a default value even if a value is not provided in the function call for that argument.'''
#e.g:
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")

#Keyword arguments:
'''We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter
name.Hence, the order in which the arguments are passed does not matter.'''
#e.g:
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

#Required arguments:
'''
In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in
the correct positional order and the number of arguments passed should match with the actual function definition.

'Example 1: when the number of arguments passed does not match the actual function definition.'
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)
 
name("Peter", "Quill")

Output:

name("Peter", "Quill")
TypeError: name() missing 1 required positional argument: 'lname' '''

#e.g2:when the number of arguments passed matches the actual function definition.
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")

#Variable-length arguments:
'''
Sometimes we may need to pass more arguments than those defined in the actual function.
This can be done using variable-length arguments.

There are two ways to achieve this:'''
#1.Arbitrary Arguments:
'''
While creating a function, pass a * before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of a tuple.'''
#e.g:
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

#2.Keyword Arbitrary Arguments:
'''
While creating a function, pass a ** before the parameter name while defining the function.
The function accesses the arguments by processing them in the form of a dictionary.'''
#e.g:
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")