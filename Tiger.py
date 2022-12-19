from BaseAnimal import *

class Tiger(BaseAnimal):

    def __init__(self, name, age):
        super().__init__("Tiger", name, age, ["savanna", "jungles"], 8, 20, ["meat"], True, "roarrrrrrr")