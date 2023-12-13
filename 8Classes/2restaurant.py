from dish import Dish


class Restaurant:
    def __init__(self, num_guests):
        self.num_guests = num_guests
        self.fridge = []

    def add_dish(self, dish):
        """
        Adds a Dish object to the fridge
        """
        if isinstance(dish, Dish):
            self.fridge.append(dish)

    def get_fridge(self):
        """
        Returns the list of Dish objects in the fridge
        """
        return self.fridge

    def serve_food(self):
        """
        Serves the first available dish to each of the guests, and returns a list of dish names served.
        If there is not enough food available for all guests, feed as many guests as possible.

        Example:

        Fridge before serving: [(Salad: 2), (Curry: 4)]
        num_guests = 3
        Fridge after serving: [(Salad: 0), (Curry: 3)]

        Example Return Value:
        ["Salad", "Salad", "Curry"]

        Explanation:
        Guest 0 is served Salad
        Guest 1 is served Salad
        Guest 2 is served Curry
        """
        # this solution starts with the number of guests we have and decriment it down based on the dishes consumed

        # just in case it doesnt want us to mess with the actual self.num_guests
        num_of_guests = self.num_guests
        names_of_dishes = []
        
        i = 0
        # if either of these conditions break the loop will end, we either run out of guests to serve, or we run out of food to give them
        while num_of_guests > 0 and i < len(self.fridge):
            curr_dish = self.fridge[i]

            if curr_dish.quantity > 0:
                dishes_served = 0

                # if there are more dishes then there are guests then we just subtract the guests from the total dishes and guests will be reduced to 0
                if num_of_guests < curr_dish.quantity:
                    dishes_served = num_of_guests

                # otherwise there are more guests than there are dishes so you just want the dishes to all be remomved (since the guests will sill over till the next dishes)
                else: #num_of_guests >= curr_dish.quantity:
                    dishes_served = curr_dish.get_quantity()

                # now we just do a count controlled loop to individually add the strings and consuming the meals 1 by 1
                j = 0
                while j < dishes_served:
                    names_of_dishes.append(curr_dish.name)
                    # testcases require you to use the dish methods in here
                    curr_dish.consume()
                    j += 1

                # finally we update our outer loop/event controlled value for guests and i
                num_of_guests -= dishes_served

            i += 1
        
        return names_of_dishes

    def has_stock(self):
        """
        Returns True if there is at least one dish that can be consumed in the fridge.
        Returns False otherwise
        """

        return len(self.fridge) > 0
        

