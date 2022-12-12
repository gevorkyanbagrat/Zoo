
from BaseAnimal import *
class Kangaroo(BaseAnimal):

#add classes
    def __init__(self, name, age):
        super().__init__("kangaroo", name, age,  ['desert', "plain", 'forest'], 3, 20, ['oats', 'nuts', 'fruits', 'grass'], False, 'GHR GHR GHR')
