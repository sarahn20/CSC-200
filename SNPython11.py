#Assignment Description:
"""
Add a roll method to DiceCollection that takes a string as a parameter and returns the result (sum of all the rolls) of rolling the dice described in the string.  
A string might look like "2D6+1D12" or "1D4" or "1D12+5D20+2D8" etc...  It only needs to support addition, but the format will always be number of dice, 
followed by a "D" followed by number of sides, then optionally a "+" followed by another roll.

"""

#Code given from class:
"""
from random import *

class DiceCollection:
  def __init__(self):
    self.theDice = []

  def add(self, aDice):
    self.theDice.append(aDice)

  def roll(self, rollString):
    # "2D6 ", "3D4+1D6"
    sum = 0
    for i in range(0, len(self.theDice)):
      sum = sum + self.theDice[i].roll()
    return sum

class Dice:
  def __init__(self, sides):
    self.sides = sides

  def roll(self):
    return randint(1, self.sides)
    
def pop(dict, key):
  if(dict.get(key) != None):
    return dict.pop()
  else:
    return None

def getNewPlayer():
  player = {}
  player["hitPoints"] = randint(10, 40)
  player["attackPower"] = randint(2,5)
  player["defense"] = randint(5, 10)
  player["bonus"] = randint(1,5)
  return player

def displayFighters(p1, p2):
  print(p1)
  print(p2)

def getAttackDamage(player):
  return randint(1, player["attackPower"])

def attack(source, destination):
  dmg = getAttackDamage(source)
  damageString = "An attack"
  if(dmg == 1):
    damageString = damageString + "grazes the opponent"
  elif(dmg == source["attackPower"]):
    damageString = damageString + "liquifies the opponent"
  else:
    damageString = damageString + "damages the opponent"

  print(damageString)
  destination["hitPoints"] = destination["hitPoints"] - dmg

def fightToTheDeath(p1, p2):
  displayFighters(p1, p2)
  turn = 0

  while(p1["hitPoints"] > 0 and p2["hitPoints"] > 0:
    if(turn % 2 == 0):
      attack(p1, p2)
    else:
      attack(p2, p1)
    turn = turn + 1
    displayFighters(p1, p2)

player1 = getNewPlayer()
player2 = getNewPlayer()
#displayFighters(player1,player2)
#fightToTheDeath(player1,player2)
myDiceBag = DiceCollection()
d6 = Dice(6)
d20 = Dice(20)
myDiceBag.add(d6)
myDiceBag.add(d20)
myDiceBag.add(Dice(12))
print(myDiceBag.roll())
"""    

#My Code:

from random import *

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

class DiceCollection:
    def __init__(self):
        self.theDice = []

    def add(self, aDice):
        self.theDice.append(aDice)

    def roll(self, rollString):
        self.numofDice = ""
        self.havehitDice = ""
        self.sides = ""
        for i in range(0,len(rollString)):
            if rollString[i] == "D":
                self.havehitDice = self.havehitDice + rollString[i]
            elif rollString[i] == "+":
                self.numofDice = int(self.numofDice)
                while self.numofDice >= 1:
                    self.add(Dice(int(self.sides)))
                    self.numofDice = self.numofDice - 1
                self.numofDice = ""
                self.havehitDice = ""
                self.sides = ""
            else:
                if self.havehitDice == "":
                    self.numofDice = self.numofDice + rollString[i]
                else:
                    self.sides = self.sides + rollString[i]
        self.numofDice = int(self.numofDice)
        while self.numofDice >= 1:
            self.add(Dice(int(self.sides)))
            self.numofDice = self.numofDice - 1
        sum = 0
        for i in range(0, len(self.theDice)):
            sum = sum + self.theDice[i].roll()
        return sum

myDiceBag = DiceCollection()
print(myDiceBag.roll("1D12+5D20+2D8"))
