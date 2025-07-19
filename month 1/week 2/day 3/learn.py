#Python Try Except
'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.'''
#Exception Handling
'''
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:'''
try:
    print(x)
except:
    print("an error occur")
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error:

# Many Exceptions
# You can define as many exception blocks as you want,
#  e.g. if you want to execute a special block of code for a special kind of error
try:
    print(x)
except NameError:
    print("Name is not define")
except:
     print("something went wrong")

# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:
try:
    print("helllo pariskhan")
except NameError:
    print("name is not define")
else:
    print("nothing is wrong")

# Finally
'''The finally block, if specified, will be executed regardless if the try block raises an error or not'''
#The finally block gets executed no matter if the try block raises any errors or not:
try:
    print(x)
except:
    print("expect")
finally:
    print("it print no matter error or not")

# e.g
#The try block will raise an error when trying to write to a read-only file:

try:
    f = open("data.txt")
    try:
        f.write("hello world")
    except:
        print("something is wrong")
    finally:
        f.close()
except:
    print("something is wrong")

# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.
# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
