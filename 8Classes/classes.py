# names = ["apple", "orange", "banana"]
# colour = ["red", "orange", "yellow"]
# sweetness = ["sweet", "sour", "sweet"]


class Fruit:
    def __init__(self, name, sweetness, colour):
        self.name = name
        self.sweetness = sweetness
        self.colour = colour
    
    def give_description(self):
        return f"i am a {self.name}, i am {self.sweetness}, and my colour is {self.colour}"

apple = Fruit("apple", "sweet", "red")

print(apple.give_description())
