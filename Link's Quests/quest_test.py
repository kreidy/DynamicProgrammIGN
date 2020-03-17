import unittest
from quest import *

class TestQuestMethods(unittest.TestCase):

    def test_continuous(self):
        availableQuests = [
            Quest("quest1",1,2,100),
            Quest("quest2",3,1,100),
            Quest("quest3",4,2,100),
        ]
        bestQuests, bestValue = chooseBestQuests(availableQuests)
        self.assertEqual(bestQuests, ["quest1", "quest2", "quest3"])
        self.assertEqual(bestValue, 300)

    def test_chooseBetterTestOnSameDay(self):
        availableQuests = [
            Quest("quest1",1,2,100),
            Quest("quest2",1,2,300),
        ]
        bestQuests, bestValue = chooseBestQuests(availableQuests)
        self.assertEqual(bestQuests, ["quest2"])
        self.assertEqual(bestValue, 300)

    def test_chooseBetterTestNextDay(self):
        availableQuests = [
            Quest("quest1",1,2,100),
            Quest("quest2",2,2,300)
        ]
        bestQuests, bestValue = chooseBestQuests(availableQuests)
        self.assertEqual(bestQuests, ["quest2"])
        self.assertEqual(bestValue, 300)

    def test_complexDecision(self):
        availableQuests = [
            Quest("quest1",1,2,200),
            Quest("quest2",1,3,400),
            Quest("quest3",3,2,100),
            Quest("quest4",3,1,250),
            Quest("quest5",4,2,500),
            Quest("quest6",5,1,600),
        ]
        bestQuests, bestValue = chooseBestQuests(availableQuests)
        self.assertEqual(bestQuests, ["quest1","quest4","quest6"])
        self.assertEqual(bestValue, 1050)

if __name__ == '__main__':
    unittest.main()
