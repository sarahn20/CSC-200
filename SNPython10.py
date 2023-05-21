#Assignment Description:
"""
Add some randomness to our fight

    Randomize who attacks first
    Randomize how hard someone hits
        Perhaps a random number between 1 and attackPower
    Build in a dodge system
        Perhaps an attack only lands if some random value is higher than the target’s defense

Add color commentary to the fight so that there is some verbiage based on misses, as well as how hard hits are.
"""

#Code give from class:
"""
from random import *

def pop(dict, key):
    if(dict.get(key) != None):
        return dict.pop()
    else:
        return None
    
def getNewPlayer():
    player = {}
    player["hitPoints"] = randint(10, 40)
    player["attackPower"] = randint(2, 5)
    player["defense"] = randint(5, 10)
    player["bonus"] = randint(1, 5)
    return player

def displayFighters(p1, p2):
    print(p1)
    print(p2)

def fightToTheDeath(p1, p2):
    displayFighters(p1, p2)
    turn = 0

    while(p1["hitPoints"] > 0 and p2["hitPoints"] > 0):
        if(turn % 2 == 0):
            p2["hitPoints"] = p2["hitPoints"] - p1["attackPower"]
        else:
            p1["hitPoints"] = p1["hitPoints"] - p2["attackPower"]
        turn = turn + 1
        displayFighters(p1, p2)

player1 = getNewPlayer()
player2 = getNewPlayer()
displayFighters(player1,player2)
fightToTheDeath(player1,player2)
"""

#My Code:

from random import *
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
    player["attackDamage"] = randint(1,player["attackPower"])
    return player
def displayFighters(p1, p2):
    print("Player 1 Stats:",p1)
    print("Player 2 Stats:",p2)
def fightToTheDeath(p1, p2):
  displayFighters(p1, p2)
    #Random generator for which player goes first
  turn = randint(1,1000)
    #Random generator for either player if they dodge their opponent's hit or not
  dodgeSystem = randint(1,25)
    #Decides who goes first
  while(p1["hitPoints"] > 0 and p2["hitPoints"] > 0):
    #For the player who goes first
    if(turn % 2 == 0):
      #If the first player's opponent doesn't dodge
      if dodgeSystem < p2["defense"]:
        p2["hitPoints"] = p2["hitPoints"] - p1["attackDamage"]
        #Statements for magnitude of Player 1 attack damage
        if p1["attackDamage"] == p1["attackPower"]:
          print("Player 1 DECIMATES Player 2 with attack damage", p1["attackDamage"], ", knocking Player 2's hit points down to ", p2["hitPoints"], "!")
          p1["attackDamage"] = randint(1,p1["attackPower"])
          p2["attackDamage"] = randint(1,p2["attackPower"])
          displayFighters(p1, p2)
          turn = randint(1,1000)
          dodgeSystem = randint(1,25)
        else:
          print("Player 1 grazes Player 2 with attack damage", p1["attackDamage"], ", knocking Player 2's hit points down to ", p2["hitPoints"], "!")
          p1["attackDamage"] = randint(1,p1["attackPower"])
          p2["attackDamage"] = randint(1,p2["attackPower"])
          displayFighters(p1, p2)
          turn = randint(1,1000)
          dodgeSystem = randint(1,25)
      #If the first player's opponent DOES dodge
      else:
        print("Player 1 attacks with damage", p1["attackDamage"], "and Player 2 DODGES!!")
        p1["attackDamage"] = randint(1,p1["attackPower"])
        p2["attackDamage"] = randint(1,p2["attackPower"])
        displayFighters(p1, p2)
        turn = randint(1,1000)
        dodgeSystem = randint(1,25)
    #For the player who goes second
    else:
      #If the second player's opponent doesn't dodge
      if dodgeSystem < p1["defense"]:
        p1["hitPoints"] = p1["hitPoints"] - p2["attackDamage"]
        #Statements for magnitude of Player 2 attack damage
        if p2["attackDamage"] == p2["attackPower"]:
          print("Player 2 DECIMATES Player 1 with attack damage", p2["attackDamage"], ", knocking Player 1's hit points down to ", p1["hitPoints"], "!")
          p1["attackDamage"] = randint(1,p1["attackPower"])
          p2["attackDamage"] = randint(1,p2["attackPower"])
          displayFighters(p1, p2)
          turn = randint(1,1000)
          dodgeSystem = randint(1,25)
        else:
          print("Player 2 grazes Player 1 with attack damage", p2["attackDamage"], ", knocking Player 1's hit points down to ", p1["hitPoints"], "!")
          p1["attackDamage"] = randint(1,p1["attackPower"])
          p2["attackDamage"] = randint(1,p2["attackPower"])
          displayFighters(p1, p2)
          turn = randint(1,1000)
          dodgeSystem = randint(1,25)
      #If the second player's opponent DOES dodge
      else:
        print("Player 2 attacks with damage", p2["attackDamage"], "and Player 1 DODGES!!")
        p1["attackDamage"] = randint(1,p1["attackPower"])
        p2["attackDamage"] = randint(1,p2["attackPower"])
        displayFighters(p1, p2)
        turn = randint(1,1000)
        dodgeSystem = randint(1,25)
player1 = getNewPlayer()
player2 = getNewPlayer()
fightToTheDeath(player1,player2)
