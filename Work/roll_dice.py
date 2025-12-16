import random

print("Welcome to the Game of rolling Dice !")

print("Enter --> Roll the Dice")
print("q --> Quit the Game")
while True:
    choice = input("Enter your choice: ")
    
    if choice == 'q':
        print("thanks for Playing the Game! bye!")
        break
        
    elif choice == '':
        dice = random.randint(1,6)
        if dice == 1:
            print("   \n * \n   ")
        elif dice == 2:
            print("*  \n   \n  *")
        elif dice == 3:
            print(" * \n * \n * ")
        elif dice == 4:
            print("* *\n   \n* *")
        elif dice == 5:
             print("* *\n * \n* *")
        elif dice == 6:
            print("* *\n* *\n* *")
    