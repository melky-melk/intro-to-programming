# NOTE THIS SOLUTION DOESNT CHANGE ANY OF THE DICE OR PLAYER CLASSES

import dice
import player
import sys

N_DICES = 2
GOAL_SCORE = 100
DEFAULT_LIMIT = 15

def setup_game():

    # Initialize two dice
    dices = [0]*N_DICES
    i = 0
    while i < N_DICES:
        dices[i] = dice.Dice()
        i += 1

    # Initialize a list of players
    name = input("What is your name human? ")
    human_player = player.Player(name)
    computer_player = player.Player("Computer")
    print(f"Hi, {human_player}.")
    
    players = (human_player, computer_player)

    return dices, players

def quit_game():
    print("See you again.")

def pprint_dices(dices):
    str_out = ""
    for i in dices:
        str_out += str(i) + " "
    return str_out.strip()

def instructions():
    str_out = ""
    str_out += (f"The  first player that reaches {GOAL_SCORE} wins.\n")
    str_out += ("Enter 'r' to roll the dice.\n")
    str_out += ("-If you roll a '1', you lose all your points for the roll and your turn.\n")
    str_out += ("-If you roll two '1's, you lose all your score and your turn.\n")
    str_out += ("Enter 'h' to hold your points and pass the turn to the next player.\n")
    str_out += ("Enter 'q' at any time to quit the game.\n")
    str_out += ("Humans go first.")
    return str_out


def set_computer_limit(args):
    '''
    Updates the computer limit to second command line argument
    Parameters:
        args: list
    Returns:
        new_limit: int
    '''
    
    limit = int(args[1])
    # we want to raise an exception if it is less than or equal to 0
    if limit <= 0:
        raise ArithmeticError("Must be a positive integer")
        # print("ValueError: Must be a positive integer")
        return DEFAULT_LIMIT

    return limit

def player_roll(player, dices):
    player.roll_dice(dices)

    # keep track of the number of 1s we rolled
    curr_total = 0
    num_of_ones = 0
    rolled_str = "You have rolled: "
    # loop through the dice and see what we rolled
    for dice in dices:
        rolled_str += dice.__str__() + " "
        
        # if its a 1 we just add to our counter without adding to total
        if dice.top_face == 1:
            num_of_ones += 1
        # if its anything else it can add to their current total 
        else:
            curr_total += dice.top_face
    
    rolled_str = rolled_str.strip(" ") # get rid of extra whitespace
    print(rolled_str)

    # if they rolled 2 1's then we reset their entire score to 0
    if num_of_ones == len(dices):
        player.score = 0
    # if they rolled any 1's then their current total for this turn is 0 (this will include if they rolled 2 1s) then their current turn total is 0
    if num_of_ones >= 1:
        curr_total = 0
    
    # now we return their total so the outer functions can decide what to do with it
    return curr_total
    
def human_turn(player, dices):
    # lets keep a flag to check if the player has rolled yet, this is needed for the hold command
    rolled_yet = False
    turn_total = 0

    # we ask for inputs infinetly unless this loop is broken by a return or break statement
    while True:
        action = input("What do you want to do ('q' to quit game, 'r' to roll, 'h' to hold)? ").lower()

        # this return false will edit the outside factors where this function is used
        if action == "q":
            quit_game()
            return False

        elif action == "r":
            # we updated our flag to true so that we can now hold our turn 
            rolled_yet = True
            roll_total = player_roll(player, dices)
            # if they rolled a 1 then we want to break (since there is no other way to get a roll_total of 0 for player_roll we can assume that they got this by rolling a 1)
            if roll_total == 0:
                turn_total = 0
                # can use break or return true here
                return True
                # break
            else:
                turn_total += roll_total
        
        elif action == "h":
            # if the rolled yet function still has not been changed to true, then we just want to print you have not rolled yet
            # since we do this without breaking the loop will go back to the top
            if rolled_yet == False:
                print("You have not rolled the dice yet.")
                continue #this continue is not necessary but its nice for clarity sake so we know it will immediately go back to the top of the function
            else:
                # otherwise if they have already rolled we can break the loop 
                break
        
        # if none of the answers were correct then we just want to print this then go back to the top of the loop
        else:
            print("I don't understand...")

    player.update_score(turn_total)
    return True

def computer_turn(computer, dices, limit):
    turn_total = 0
    # the computer keeps rolling until they hit their limit at which point they will hold
    while turn_total < limit:
        roll_total = player_roll(computer, dices)

        # if they rolled a 1 then return before the score can be updated
        if roll_total == 0:
            return
        
        turn_total += roll_total

    # at the end of their turn, update the score
    computer.update_score(turn_total)

def main(args):
    '''
    Implementation of Two-Dice Pig game.
    '''
    limit = DEFAULT_LIMIT
    try:
        limit = set_computer_limit(args)
    except ArithmeticError:
        print("ValueError: Must be a positive integer.")
    except IndexError:
        print("IndexError: list index out of range")
    except ValueError:
        print("ValueError: invalid literal for int() with base 10: 'text'")

    # break up our outouts into better named variables
    dices, players = setup_game()
    # same for the players
    human, computer = players

    print(instructions()) 

    # lets set our current player to the human since they go first 
    curr_player = human
    # lets also set game running to true, so the human can modify it and so this while loop will continue infinetly until it is changed
    game_running = True
    while game_running:
        # this should print through every time a new turn is taken
        print(f"Score: {human.name} - {human.score}, {computer.name} - {computer.score}")
        print(f"It is now {curr_player.name} turn...")

        # now we use the current player to change the behaviour of what the game should do for each plater
        if curr_player == human:
            # human_turn returns true or false based on whether or not they qanted to quit the game, if they quit it is false 
            # in all other cases it is true. human turn will also ask for inputs
            game_running = human_turn(human, dices)
        # whereas computer turn will run autmatically and keep rolling until they hit their limit
        elif curr_player == computer:
            computer_turn(computer, dices, limit)

        # checks if either of the players won
        if curr_player.score >= 100:
            print(f"{curr_player.name} wins!")
            game_running = False # set to false so the loop will exit

        # switch players at the very end of the turn, if it was the computer then we want to switch to human
        # otherwise (if it was the human) we want to switch to computer
        if curr_player == computer:
            curr_player = human
        else:
            curr_player = computer
        # the below is a line of code which is just a cleaner way to write the above, its called a ternary statement its like a condensed if statement
        # curr_player = computer if curr_player == human else human

# DO NOT REMOVE
if __name__ == "__main__":
    main(sys.argv)
