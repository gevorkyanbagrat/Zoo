class Kangaroo:

    byome=['desert', 'plain', 'forest']
    area=20
    food=['oats', 'nuts', 'fruits', 'grass']
    predator=False
    sound='GHR GHR GHR'


    def __init__(self, name, amountOfFood, age):
        self.__Name = name
        self.__AmountOfFood = amountOfFood
        self.__Age = age
        self.__byome = ['desert', 'plain', 'forest']
        self.__area = 20
        self.__Food = ['oats', 'nuts', 'fruits', 'grass']
        self.__predator = False
        self.__sound = 'GHR GHR GHR'
        self.__foodCount = 0
        self.IsFeeded = False

    def DoSound(self, number):
        for i in range(number):
            print(self.Name, self.sound)

    def Eat(self, Food):
        if Food in self.__Food:
            self.__foodCount += 1
            if self.__foodCount == self.__AmountOfFood:
                self.IsFeeded = True
                print("Я наелся")
        else:
            print('Я не ем такое')

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, name):
        self.__Name = name

    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self, value):
        self.__Age = value

    @property
    def Byome(self):
        return self.__Byome

    @property
    def Area(self):
        return self.__area

    @property
    def Food(self):
        return self.__Food

    @Food.setter
    def Food(self, unitOfFood):
        self.__Food.append(unitOfFood)