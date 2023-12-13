from dice import Dice
from player import Player

N_DICES = 2

def setup_game():
    '''
    Generates the Dice and Player objects needed for the game.
    '''
    # Initialize a list of two Dice objects
    dices = [0]*N_DICES
    i = 0
    while i < N_DICES:
        dices[i] = Dice()
        i += 1

    # Initialize a list of Player objects
    name = input("What is your name human? ")
    human_player = Player(name)
    computer_player = Player("Computer")
    print(f"Hi, {human_player}.")
    
    players = (human_player, computer_player)

    return dices, players


def print_dices(dices):
    str_out = ""
    for i in dices:
        str_out += str(i) + " "
    return str_out.strip()

def main():
    # result = setup_game()
    # dices = result[0]
    # player = result[1]
    # assign the return values from the function to the variables dices and players
    dices, players = setup_game()

    # since players is also a tuple we can split that into the 2 players we have, the human and the CPU
    human, CPU = players

    # Instructions
    print("The player with highest roll wins.")
    print("Humans go first. ")

    # asking the player for a yes or no only, then it breaks. the action is saved when the loop ends
    action = None
    while True:
        action = input("Do you want to roll the dice [Y|N]? ")

        action = action.strip().lower()
        if action == "y" or action == "n":
            break
        
        print("I don't understand...")
    
    # if yes the player will roll the dice
    if action == "y":
        # goes into the player function, where it takes the dice list and rolls it adding to the tally
        human.roll_dice(dices)
    # otherwise the computer will print this line
    elif action == "n":
        # If the human does not want to roll, we manually set their rolled history, since dice start with a top face of 1
        # we can just set the rolled history to the dices without rolling it
        # this way, the human still has a rolled history of 1 1 
        human.set_rolled_history(dices)
        print("Ok. I will roll then.")

    # the computer will roll the dice regardless of what the player decides 
    # so its outside of the if statements
    CPU.roll_dice(dices)

    # then we call on the methods to internally update the score
    human.update_score()
    CPU.update_score()

    # I made a new function inside player to do this whole print statement for me, so we can just use that 
    print(human.get_results())
    print(CPU.get_results())
    # print(f"{human.name} rolls: {human.rolled_history[0]} {human.rolled_history[0]}")
    # print(f"Computer rolls: {computer_dice1} {computer_dice2}")

    winner = None
    if human.score > CPU.score:
        winner = human
    elif CPU.score > human.score:
        winner = CPU

    # this is a ternary statement, it does the same(ish) as above it doesnt have the none statement but its super handy
    # for doing a short if statement
    # winner = human if human.score > CPU.score else CPU
    
    if winner == None:
        print("It is a draw.")
    else:
        print(f"{winner.name} wins.")

    # you can also do it this way
    # Decide winner
    # if human.score > CPU.score:
    #     print(f"{human.name} wins.")
    # elif CPU.score > human.score:
    #     print("Computer wins.")
    # else:
    #     print("It is a draw.")

if __name__ == "__main__":
    main()
