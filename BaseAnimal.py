class BaseAnimal:
    def __init__(self, type,  name, age):
        self.__Byome = None
        self.__type = type
        self.__Name = name
        self.__AmountOfFood = 0
        self.__Age = age
        self.__area = 0
        self.__Food = []
        self.__predator = False
        self.__sound = ""
        self.__foodCount = 0
        self.IsFeeded = False

    def DoSound(self, number):
        for i in range(number):
            print(self.Name, self.__sound)

    def Eat(self, Food):
        if Food in self.__Food:
            if self.__foodCount > self.__AmountOfFood:
                print(self.__Name, "я наелся и больше не буду")
            else:
                self.__foodCount += 1
            if self.__foodCount == self.__AmountOfFood:
                self.IsFeeded = True
                print(self.__Name,"Я наелся")
            elif self.__foodCount > self.__AmountOfFood:
                print(self.__Name,"я наелся и больше не буду")
        else:
            print(self.__Name,'Я не ем такое')


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
    def Sound(self):
        return self.__sound

    @Sound.setter
    def Sound(self, sound):
        self.__sound=sound
    @property
    def Byome(self):
        return self.__Byome

    @Byome.setter
    def Byome(self, byome):
        self.__Byome = byome

    @property
    def Area(self):
        return self.__area
    @Area.setter
    def Area(self, area):
        self.__area=area

    @property
    def Food(self):
        return self.__Food

    @Food.setter
    def Food(self, unitOfFood):
        self.__Food.append(unitOfFood)

    @property
    def type(self):
        return self.__type

    @property
    def amountOfFood(self):
        return self.__AmountOfFood

    @amountOfFood.setter
    def amountOfFood(self, amountOfFood):
        self.__AmountOfFood=amountOfFood

