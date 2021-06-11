# Python's built-in module that you can use to make random numbers.
import random

# Initialise players scores to 0
player_1_score = 0
player_2_score = 0

# Initialise counter to count the number of rounds to 0 
count=0

# for loop to repeat block of code for 5 times
for i in range(5):
    
    # Increment the counter by 1 everytime
    count+=1
    print('Round:',count)
    print('--------')
    
    #returns a number between 1 and 6 (both included)
    player_1_score = random.randint(1,6)
    player_2_score = random.randint(1,6)
    
    # print the scores of the players
    print('Player 1 rolled: ',player_1_score)
    print('Player 2 rolled: ',player_2_score)
    
    # if to evaluate test conditions:
    if player_1_score > player_2_score:
        player_1_score += 1
        print('Winner is player 1')
    elif player_2_score > player_1_score:
        player_2_score += 1
        print('Winner is player 2')
    else:
        print('Its a draw')
    print( )

# print final scores
print('Final Scores:')
print('Player 1 Score: ',player_1_score )
print('Player 2 Score: ',player_2_score )