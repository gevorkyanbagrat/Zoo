from Goat import *
from Monkey import *
from Kangaroo import *
g=Goat("Чик", 4)
g.DoSound(5)
print(g.Name, g.Age, g.Food, g.Byome, g.Area, g.type)
print(g.amountOfFood, g.IsFeeded)
g.Eat("трава")
g.Eat("трава")
g.Eat("трава")
g.Eat("рога")



