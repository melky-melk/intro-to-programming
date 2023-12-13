import random

class Dice:
    def __init__(self):
        self.top_face = 1

    def set_top_face(self, num):
        '''
        Sets the value for top_face of the dice.
        num must be integer and falls within the range of 1 and 6.
        Parameters:
            num: int, number indicating new value of top face of dice.
        Returns:
            success: bool, True if set successfully. Else, False.
        '''
        # check if it is a valid number, if not then just return so it will not do the proceeding lines
        if not (num >= 1 and num <= 6):
            return False
        
        # once valid set thetop face to the number givern
        self.top_face = num
        return True
    
    def roll_dice(self):
        '''
        Updates top_face with a random number between 1 and 6.
        '''
        self.set_top_face(random.randint(1,6))

    def __str__(self):
        return f"{self.top_face}"
