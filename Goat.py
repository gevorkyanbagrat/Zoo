class Goat:

    byome='plain'
    area=10
    food='grass'
    predator=False
    sound='Noone can stop me I feel like the greatest'


    def __init__(self, name, amountOfFood, age):
        self.Name=name
        self.Amount=amountOfFood
        self.Age=age


    def DoSound(self, number):
        for i in range(number):
            print(self.Name, self.sound)

    def Eat(self, Food):
        Food-=self.amountOfFood
