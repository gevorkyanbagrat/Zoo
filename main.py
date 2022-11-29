from Goat import *
goat1=Goat("Русик", 2, 4)
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

