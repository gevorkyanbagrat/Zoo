class Aviary:
    def __init__(self, name, area, biome):
        self.__name = name
        self.__area = area
        self.__biome = biome
        self.__feeders= []

        self.__listOfAnimals = []

    def AddAnimal(self, animal):

        if not(self.__area >= animal.Area and self.__biome in animal.Biome):
            print("этот зверь не подходит к такому вольеру1")

            return

        if len(self.__listOfAnimals) > 0:
            if not(self.__listOfAnimals[0].predator == False and animal.predator == False):
                print("этот зверь не подходит к такому вольеру2")
                return
                if not (self.__listOfAnimals[0].type == animal.type):
                    print("этот зверь не подходит к такому вольеру3")
                    return

        self.__listOfAnimals.append(animal)
        animal.inAviary = self

    def DeleteAnimal(self, animal):
        if animal in self.__listOfAnimals:
            self.__listOfAnimals.remove(animal)
            self.__area+=animal.Area
            animal.inAviary = 0
        else: print("этого животного нет в данном вольере")

    def AddFeeder(self,feeder):
        self.__feeders.append(feeder)

    def FullFeeders(self, food, amount):
        for i in self.__feeders:
            i.full(food, amount)

    def FullParticularFeeder(self, numberOfFeeder, food, amount):
        self.__feeders[numberOfFeeder].full(food, amount)

    def Eat(self):
        for a in self.__listOfAnimals:
            if a.IsFeeded == False:
                for f in self.__feeders:
                    for food in f.Food:
                        if food in a.Food:
                            if a.foodCount > a.amountOfFood:
                                print(a.Name, "я наелся и больше не буду")
                            elif a.foodCount == a.amountOfFood:
                                a.IsFeeded = True
                                print(a.Name,"Я наелся")
                            else:
                                a.foodCount += 1
                                if a.foodCount == a.amountOfFood:
                                    a.IsFeeded = True
                                    print(a.Name, "Я наелся")
                        else:
                            print(a.Name,'Я не ем такое', food)

    def FindWhoWantToEat(self):
        for i in self.__listOfAnimals:
            if i.IsFeeded == False:
                print(i.Name, "хочет есть", i.Food, i.amountOfFood-i.foodCount)
    @property
    def listOfAnimals(self):
        return self.__listOfAnimals

    @property
    def Feeders(self):
        return self.__feeders