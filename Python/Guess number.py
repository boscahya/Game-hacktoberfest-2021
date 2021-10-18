# Manish Bishowkarma
# 18, October, 2021
# Two Player Guess the Number Game

print("\n\n\tWelcome to 'Guess My Number !'")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess  it in as few attempts as possible.\n")

# Initial Values
import random
number=random.randint(1,100)
guess= 0
tries = 1

# Creating player's
while guess != number:
    guess=int(input("Take a Guess:"))
    if guess > number:
            print("Player guess lower....")
            
    elif guess < number:
            print("player guess higher..")
        
    elif guess==number:
            print("Congratulations!!!You wins..")
            break
            tries = tries + 1    
    
# Creating Computer's turn

    guess=random.randint(1,100)
    print("\nComputer has guessed:",guess)

    if guess > number:
        print("Computer guess lower..\n")
   
    elif guess < number:
        print("Computer guess higher..\n")
           
    elif guess==number:
        print("Game Over! Congratulatuions!!! Computer wins..")
        
        tries = tries + 1

input("\n\nPress enter to continue.")






     
     
        
        
        
        


