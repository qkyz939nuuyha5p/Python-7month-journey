#number guessing game using while loop...
import random
secret = random.randint(1, 10)
guess = 0
while guess != secret:
    num = int(input("Enter the number:"))
    if num > secret:
        print("too high!")
    elif num < secret:
        print("too low!")
    else:
        print("correct")
        break