#python loops....
'''
Python has two primitive loop commands:
1.while loops
2.for loops
'''
#while loops
'''
As the name suggests, while loops execute statements while the condition is True.
 As soon as the condition becomes False, the interpreter comes out of the while loop.
'''
a = 1
while(a<=5):
    print(a)
    a+=1

#break statement(With the break statement we can stop the loop even if the while condition is true:)
a = 1
while(a<=5):
    print(a)
    if a==3:
        break
    a+=1

#Continue statement(With the continue statement we can stop the current iteration, and continue with the next:)
x = 10
while(x>0):  
    x = x-1
    if x == 6:
        continue
    print(x)

#else statement(With the else statement we can run a block of code once when the condition no longer is true:)
i=0
while(i<6):
    print(i)
    i+=1
else:
    print("no longer less than 6")