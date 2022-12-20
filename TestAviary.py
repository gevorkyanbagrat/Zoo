import unittest
from Goat import *
from Tiger import *
from Lion import *
from Aviary import *
from Kangaroo import *
from Monkey import *
from Zoo import *



class TestAviay(unittest.TestCase):
    def setUp(self):
        self._testAviaryBigAreaPlain = Aviary("TestName1", 100, "plain")
        self._testAviarySmallAreaPlain = Aviary("TestName1", 10, "plain")
        self._testAviaryBigAreaSavanna = Aviary("TestName1", 100, "savnna")
        self._testAviaryBigAreaDesert = Aviary("TestName1", 100, "desert")
        self._testGoat = Goat("testGoat1", 1)
        self._testMonkey = Monkey("testMonkey1", 1)
        self._testKangaroo = Kangaroo("testKangaroo1", 1)
        self._testTiger = Tiger("testTiger1", 1)
        self._testLion = Lion("testLion1", 1)

    def testAddAnimal(self):
        aviary=self._testAviaryBigAreaPlain
        animal=self._testTiger
        expected = len(aviary.listOfAnimals)-1
        aviary.AddAnimal(animal)
        actual = len(aviary.listOfAnimals)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
