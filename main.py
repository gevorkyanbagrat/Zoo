from Goat import *
from Monkey import *
from Kangaroo import *
goat1=Goat("Русик", amountOfFood=3, age=4)
goat1.DoSound(5)
print(goat1.Name)
goat1.Name= 'edit'
print(goat1.Name)
print(goat1.Age)
goat1.Age=8
print(goat1.Age)
goat1.Food= 'яблоко'
print(goat1.Food)
goat1.Eat('яблоко')
print(goat1.IsFeeded)
goat1.Eat('як')
print(goat1.IsFeeded)


monkey1 = Monkey("Кура", amountOfFood=2, age=2)
print(monkey1.Name)
monkey1.Eat('grape')
monkey1.Eat('grape')
monkey1.Eat('grape')
monkey1.Eat('meat')
print(monkey1.IsFeeded)

kangaroo1=Kangaroo("Рамзес", amountOfFood=4, age=1)
print(kangaroo1.Name)
kangaroo1.DoSound(2)
kangaroo1.Eat('oats')
kangaroo1.Eat('oats')
kangaroo1.Eat('oats')
kangaroo1.Eat('oats')
print(kangaroo1.IsFeeded)

