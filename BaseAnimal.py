class BaseAnimal:
    def __init__(self, type,  name, age, biome, amountOfFood, area, food, predator, sound):
        self.__Biome = biome
        self.__type = type
        self.__Name = name
        self.__AmountOfFood = amountOfFood
        self.__Age = age
        self.__area = area
        self.__Food = food
        self.__predator = predator
        self.__sound =  sound
        self.__foodCount = 0
        self.__IsFeeded = 0
        self.__inAviary = 0

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
                self.__IsFeeded = True
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
    def Biome(self):
        return self.__Biome

    @Biome.setter
    def Biome(self, biome):
        self.__Biome = biome

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


    @property
    def predator(self):
        return self.__predator

    @property
    def InAviary(self):
        return self.__inAviary

    @InAviary.setter
    def InAviary(self, aviary):
        self.__inAviary = aviary

    @property
    def IsFeeded(self):
        return self.__IsFeeded
    @IsFeeded.setter
    def IsFeeded(self, booli):
        self.__IsFeeded = booli

    @property
    def foodCount(self):
        return self.__foodCount
    @foodCount.setter
    def foodCount(self, value):
        self.__foodCount=value

