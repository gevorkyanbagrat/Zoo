class Feeder():
    def __init__(self, name, typeOfFood):
        self.__name = name
        self.__typeOfFood = typeOfFood
        self.__food=[]

    @property
    def TypeOfFood(self):
        return self.__typeOfFood
    @TypeOfFood.setter
    def TypeOfFood(self, newType):
        self.__typeOfFood = newType

    @property
    def Food(self):
        return  self.__food

    def full(self, food, number):
        if food in self.__typeOfFood:
            for i in range(number):
                self.__food.append(food)
        else: print("Эта еда не подходит для данной кормушки")