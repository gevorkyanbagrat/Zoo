class Kangaroo:

    byome=['desert', 'plain', 'forest']
    area=20
    food=['oats', 'nuts', 'fruits', 'grass']
    predator=False
    sound='GHR GHR GHR'


    def __init__(self, name, amountOfFood, age):
        self.Name=name
        self.Amount=amountOfFood
        self.Age=age


    def DoSound(self, number):
        for i in range(number):
            print(self.Name, self.sound)

    def Eat(self, Food):
        Food-=self.amountOfFood
