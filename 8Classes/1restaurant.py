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
        # this solution uses more of the inbuilt functions inside of the classes already, but it has a lot of moving parts so it might be less easy to understand than 2restaurant.py (tho i do like this solution better)

        names_of_dishes = []

        # we keep count of the number of guests served 
        guests_served = 0
        # only break the loop if you have served all the guests or there is no more stock
        while guests_served < self.num_guests and self.has_stock():
        
            dish = self.fridge[0]
            # decriment dishes if it was able to be decrimented  
            if (dish.consume()):
                # then add thhat dish to the ones served.
                names_of_dishes.append(dish.name)
                # and increment guests served if the dish was consumed successfully
                guests_served += 1

            # otherwise, if dish consume returned false, then that dish has nothing left inside of it. 
            # remove it from the list so that has_stock can return false if we run out of guests
            else:
                self.fridge.pop(0)
        
        return names_of_dishes

    def has_stock(self):
        """
        Returns True if there is at least one dish that can be consumed in the fridge.
        Returns False otherwise
        """

        return len(self.fridge) > 0
        

