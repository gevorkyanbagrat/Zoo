from Goat import *
from Monkey import *
from Kangaroo import *
from Aviary import *
from Feeder import *

g = Goat("Чик", 4)
g2 = Goat("Варг", 3)
g3 = Goat("Зубрила", 3)
k1 = Kangaroo("Чентик", 6)
m1 = Monkey("Брамс", 1)
# f = Feeder("Кормушка1", ["grass", "hay"])
f2= Feeder("Кормушка2", ["meat", "fish"])
f3= Feeder("Кормушка3", ["oats"])




# g.DoSound(5)
#
# print(g.Name, g.Age, g.Food, g.Biome, g.Area, g.type)
# print(g.amountOfFood, g.IsFeeded)
#
# g.Eat("трава")
# g.Eat("трава")
# g.Eat("трава")
# g.Eat("рога")
#
v = Aviary("Рогатые и копы", 30, "plain")
v.AddAnimal(g)
v.AddAnimal(k1)
v.AddAnimal(m1)
# v.AddFeeder(f)
v.AddFeeder(f2)
v.FullFeeders("grass", 4)
v.FullFeeders("meat", 5)
# v.FullParticularFeeder(1, "fish", 6)
v.Eat()
v.FindWhoWantToEat()
f2.TypeOfFood="oats"
v.FullFeeders("oats",3)
v.Eat()
v.FindWhoWantToEat()
v.Eat()

# print(v.Feeders[0].Food)
# print(v.Feeders[1].Food)
#
#
# print(v.listOfAnimals)
# v.DeleteAnimal(g)
# print(v.listOfAnimals)
