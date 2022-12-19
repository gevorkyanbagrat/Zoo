from Aviary import*
from BaseAnimal import*
from Feeder import *



class Zoo:
  def __init__(self, name):
    self.__name= name
    self.__aviaries = []
  
  
  def AddNewAviary(self, name,  area, biome ):
    self.__aviaries.append(Aviary(name, area, biome))
    
  def AddCreatedAviary(self, aviary):
    self.__aviaries.append(aviary)

  def ManageAnimal(self, animal, newAviary):
    for i in self.__aviaries:
      if i == animal.inAviary:
        i.DeleteAnimal(animal)
      if i == newAviary:
        i.AddAnimal(animal)
        
  def PrintListOfAnimals(self):
      for i in self.__aviaries:
        for a in i.listOfAnimals:
          print(a.type, a.Name, "находится в ", i.Name)
        
        
       
    
  
