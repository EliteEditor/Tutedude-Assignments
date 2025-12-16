import random

print("!Welcome to number Guessing Game!")
print("Your secret number is between 1 to 50")

num = random.randint(1, 50)
count = 10

while count > 0:
    choice = int(input("Enter your guess: "))

    count -= 1

    if choice == num:
        print(f"You guessed right! Congrats! You won in {10 - count} attempts.")
        break
    else:
        print("Wrong guess! Try again.")
        print(f"You have {count} attempts left.\n")

if count == 0:
    print("\nOut of attempts! Better luck next time.")
    print(f"The correct number was: {num}")
