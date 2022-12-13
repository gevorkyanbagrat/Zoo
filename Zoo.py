from Aviaries import*
from BaseAnimal import*
from Feeders import *



class Zoo(name):
  
  def __init__(self, name):
    self.__name= name
    self.__aviaries = []
  
  
  def AddNewAviary(self, name,  area, biome ):
    self.__aviaries.append(Aviary(name, area, biome))
    
  def AddCreatedAviary(self, aviary):
    self.__aviaries.append(aviary)

  def ManageAnimal(self, animal, recentAviary, newAviary):
    for i in self.__aviaries:
      if i == recentaviary:
        i.DeleteAnimal(animal)
      if i == newAviary:
        i.AddAnimal(animal)
        
   def PrintListOfAnimals(self):
      for i in self.__aviaries:
        for a in i.ListOfAnimals:
          print(a.type, a.name, "находится в ", i.name)
        
        
       
    
  
