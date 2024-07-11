import random
import math

# Get lower and upper bounds from user in one input
lower, upper = map(int, input("Enter Lower and Upper bounds separated by a space: ").split())

# Generate random number between the lower and upper bounds
x = random.randint(lower, upper)

# Calculate the maximum number of guesses
total_chances = math.ceil(math.log2(upper - lower + 1))
print(f"\n\tYou have {total_chances} chances to guess the number!\n")

count = 0

# Start guessing loop
while count < total_chances:
    count += 1
    guess = int(input("Guess a number: "))

    if guess == x:
        print(f"Congratulations! You guessed it in {count} tries.")
        break
    elif guess < x:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"\nThe number was {x}. Better luck next time!")
