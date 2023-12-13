class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rolled_history = []

    def set_rolled_history(self, ls_dice):
        '''
        ...
        Parameters:
            ls_dice: list of Dice objects
        Returns:
            None
        '''
        try:
            N = len(ls_dice)
            i = 0
            while i < N:
                self.rolled_history.append(ls_dice[i].top_face)
                i += 1
        except:
            print("Must be a list of dice.")

    def roll_dice(self, ls_dice):
        '''
        ...
        Parameters:
            ls_dice: list of Dice objects
        Returns:
            None
        '''
        try:
            N = len(ls_dice)
            i = 0
            while i < N:
                ls_dice[i].roll_dice()
                i += 1
            self.set_rolled_history(ls_dice)
        except:
            print("Must be a list of dice.")

    def update_score(self):
        '''
        Calculates the total and assigns to score.
        '''
        i = 0
        total = 0
        while i < len(self.rolled_history):
            total += self.rolled_history[i]
            i += 1
        self.score = total 
    
    def __str__(self):
        return f"{self.name}"

    def get_results(self):
        string = self.name + " rolls:"

        for i in range(len(self.rolled_history)):
            string += " " + str(self.rolled_history[i])

        return string


