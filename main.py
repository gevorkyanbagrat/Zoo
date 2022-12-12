from Goat import *
from Monkey import *
from Kangaroo import *
from Aviary import*
g=Goat("Чик", 4)
g.DoSound(5)
print(g.Name, g.Age, g.Food, g.Biome, g.Area, g.type)
print(g.amountOfFood, g.IsFeeded)
g.Eat("трава")
g.Eat("трава")
g.Eat("трава")
g.Eat("рога")

v=Aviary("Рогатые и копы", 30, "plain")
v.AddAnimal(g)
print(v.listOfAnimals[0].Name)


