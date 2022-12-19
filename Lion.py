from BaseAnimal import *


class Lion(BaseAnimal):

    def __init__(self, name, age):
        super().__init__("Lion", name, age, ["savanna"], 10, 20, ["meat"], True, "Roarrrrr")
