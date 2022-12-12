class Aviary:
    def __init__(self, name, area, biome):
        self.__name = name
        self.__area = area
        self.__biome = biome

        self.__listOfAnimals = []

    def AddAnimal(self, animal):

        if not(self.__area >= animal.Area and self.__biome == animal.Biome):
            print("этот зверь не подходит к такому вольеру1")

            return

        if len(self.__listOfAnimals) > 0:
            if not(self.__listOfAnimals[0].predator == False and animal.predator == False):
                print("этот зверь не подходит к такому вольеру2")
                return
            elif not (self.__listOfAnimals[0].type == animal.type):
                print("этот зверь не подходит к такому вольеру3")
                return

        self.__listOfAnimals.append(animal)
        animal.inAviary = self

    def DeleteAnimal(self, animal):
        # if
        self.__listOfAnimals.remove(animal)
        pass

    @property
    def listOfAnimals(self):
        return self.__listOfAnimals