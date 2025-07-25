#Go weeek 1 day 6 and 7 to learn loop.
'''
*****
*****
*****
*****
*****'''
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

'''
*
**
***
****
*****'''
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    print()
    i += 1
