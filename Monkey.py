class Monkey:

    byome='jungles'
    area=50
    food=['bananas', 'grape', 'gummy', 'bugs']
    predator=False
    sound='U A U'


    def __init__(self, name, amountOfFood, age):
        self.Name=name
        self.Amount=amountOfFood
        self.Age=age


    def DoSound(self, number):
        for i in range(number):
            print(self.Name, self.sound)

    def Eat(self, Food):
        Food-=self.amountOfFood
