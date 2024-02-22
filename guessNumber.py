import random

rand = random.randint(1, 100)

n = 0
print("Try to guess number up to 100")
while (rand != n):
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        continue 
    if (rand == n):
        print(f"You guessed it right , Number you were trying to guess was: {n}")
        
    if (rand != n):
        
        if(rand > n):
            print("Try higher")
        
        elif (rand < n):
            print("Try lower")
        
    
