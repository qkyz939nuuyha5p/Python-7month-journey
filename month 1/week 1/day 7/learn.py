#for loop..
'''
A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string).
'''
#list in for loop(With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.)
fruits = ["apple", "banana", "mango"]
for x in fruits:
    print(x)

#looping through a strings..
for c in "parikshan shahi thakuri":
    print(c)

#break statement in for loop
fruits = ["1", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#continue statement in for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
'''
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number.'''
for x in range(6):
   print(x)
'''
The range() function defaults to increment the sequence by 1, 
however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):'''
for x in range(2, 30, 3):
  print(x) 
#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")
#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#Nested Loops
#A nested loop is a loop inside a loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#The pass Statement
#for loops cannot be empty, 
# but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass