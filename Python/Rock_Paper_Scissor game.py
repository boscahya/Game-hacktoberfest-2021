
import random

def toss():
    computer = random.randint(1,5)
    if computer == 1:
        return "Rock"
    elif computer == 2:
        return "Paper"
    elif computer == 3:
        return "Scissor"
    elif computer == 4:
        return "Lizard"
    elif computer == 5:
        return "Spock"
    else:
        print("Invalid Entry!")



        
# Determine winner

def determine_winner(player,computer):
    global player_win, computer_win
    if player == computer:
        return "It's a Tie!"




# player winner
    if player == computer:
        return "It's a Tie!"
    elif player =="Rock"  and computer =="Scissor":
        player_win += 1
        return "\t\tRock smashes Scissor.\n\t\t\t\t  Players Wins!"
         
    
    elif player =="Rock"  and computer =="Lizard":
        player_win += 1
        return "\t\tRock smashes Lizard.\n\t\t\t\t  Players Wins!"
        
    
    elif player =="Paper"  and computer =="Rock":
        player_win+= 1
        return "\t\tPaper covers rock.\n\t\t\t\t  Players Wins!"
       
    
    elif player =="Paper"  and computer =="Spock":
        player_win += 1
        return "\t\tPaper disproves Spock.\n\t\t\t\t  Players Wins!"
    
    
    elif player =="Scissor"  and computer =="Paper":
        player_win += 1
        return "\t\tScissor cuts Paper.\n\t\t\t\t  Players Wins!"
       
    
    elif player =="Scissor"  and computer =="Lizard":
        player_win += 1
        return "\t\tScissor decapitates Lizard.\n\t\t\t\t   Players Wins!"
      
    
    elif player =="Lizard"  and computer =="Paper":
        player_win += 1
        return "\t\tLizard eats Paper.\n\t\t\t\t  Players Wins!"
        
    
    elif player =="Lizard"  and computer =="Spock":
        player_win += 1
        return "\t\tLizard poisons Spock.\n\t\t\t\t   Players Wins!"
      
    
    elif player =="Spock"  and computer =="Rock":
        player_win += 1
        return "\t\tSpock vaporizes rock.\n\t\t\t\t   Players Wins!"
        
    
    elif player =="Spock"  and computer =="Scissor":
        player_win += 1
        return "\t\tSpock smashes Scissor.\n\t\t\t\t   Players Wins!"
        

# computer winners

    elif computer =="Rock"  and player =="Scissor":
        computer_win += 1
        return "\t\tRock smashes Scissor.\n\t\t\t\t  Computer Wins"
       
    
    elif computer =="Rock"  and player =="Lizard":
        computer_win += 1
        return "\t\tRock smashes Lizard.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Paper"  and player =="Rock":
        computer_win+= 1
        return "\t\tPaper covers rock.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Paper"  and player =="Spock":
        computer_win += 1
        return "\t\tPaper disproves Spock.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Scissor"  and player =="Paper":
        computer_win += 1
        return "\t\tScissor cuts Paper.\n\t\t\t\t  Computer Wins!"
        
     
    elif computer =="Scissor"  and player  =="Lizard":
        computer_win += 1
        return "\t\tScissor decapitates Lizard.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Lizard"  and  player =="Paper":
        computer_win += 1
        return "\t\tLizard eats Paper.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Lizard"  and  player =="Spock":
        computer_win += 1
        return "\tLizard poisons Spock.\n\t\t\t\t  Computer Wins!"

    
    elif computer =="Spock"  and  player =="Rock":
        computer_win += 1
        return "\t\tSpock vaporizes rock.\n\t\t\t\t  Computer Wins!"
        
    
    elif computer =="Spock"  and player =="Scissor":
        computer_win += 1
        return "\t\tSpock smashes Scissor.\n\t\t\t\t  Computer Wins!"


# main
response = "n"
response = "y"
player_win = 0
computer_win = 0


while response == "y":
    print("Welcome To Game!".center(80," "))
    print("\t\t\t(Rock, paper, Scissor,Lizard,Spock)")
    player = input("\n\tWhat do you want to throw(Rock,Paper,Scissor,Lizard,Spock):")

    computer = toss()


    result = "Player Threw:" + player.capitalize() + \
    "       Computer Threw:" + computer


    winner = determine_winner(player.capitalize(), computer)


    score = "Player's Score:" + str(player_win) + \
            " "*25 + "Computer's Score:" + str(computer_win) + "\n"



# print all statement
    print("\n",result.center(80," "))
    print(winner.center(80," "))
    print("\n")
    print(score.center(80," "))
    print("\n\n\n")
   
    response = input("Would you like to play again? (y/n):")
    if response == "n":
        print("\nTotal Scores!!!")
        print("# Computer:",computer_win)
        print("# Player  :",player_win)
        print("Thank you for playing.Good-Bye!")



input("\nPress enter to exit.")
    



        
