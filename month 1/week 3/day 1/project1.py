# mini project on Number guessing.
import random
secret = random.randint(1,10)
tries = 0

while tries < 5:
    number = int(input("Enter the number:"))
    if secret == number:
        print("Correct number!")
        break
    elif secret != number:
        print("Incorrect number!")
        tries+=1

else:
     print(f"❌ Out of tries. The number was {secret}.")