from BaseAnimal import *


class Goat(BaseAnimal):

    def __init__(self, name, age):
        super().__init__(Goat, name, age)
        self.Byome = "plain"
        self.Sound = "me me me"
        self.Area = 15

