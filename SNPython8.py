#Assignment Description: 
"""
Implement the getValueOfBlackJackHand function almost as described in class.  You should return the value of the hand that is the highest without going over 21.
"""
#Code given from class:
"""
from random import *

def fillListWithRandoms(lst, numberOfRandoms):
    for i in range(0, numberOfRandoms):
        lst.append(randint(1,1000))
    print(lst)

def splitCommaDelimStringToList(s):
    currentString = ""
    lst = []
    for i in range(0, len(s)):
        if(s[i] != ','):
            currentString = currentString + s[i]
        else:
            lst.append(currentString)
            currentString = ""
    lst.append(currentString)
    return lst

def getDeckOfCards():
    cardVals = splitCommaDelimStringToList("2,3,4,5,6,7,8,9,10,J,Q,K,A,Joker")
    deck = []
    for i in range(0, len(cardVals)):
        deck.append(cardVals[i])
        deck.append(cardVals[i])
        deck.append(cardVals[i])
        deck.append(cardVals[i])
    return deck

def shuffleDeck(deck):
    for i in range(0, 1000):
        cardPos1 = randint(0, len(deck)-1)
        cardPos2 = randint(0, len(deck)-1)
        tempCard = deck[cardPos1]
        deck[cardPos1] = deck[cardPos2]
        deck[cardPos2] = tempCard

def dealCard(deck):
    return deck.pop()

def dealABlackJackHand(deck):
    hand = []
    hand.append(dealCard(deck))
    hand.append(dealCard(deck))
    return hand

def getValueOfBlackJackHand(hand):
    #return a list of the possible values of the hand
    #number cards have a value that is their number
    #face cards (J, Q, K) - have a value of 10
    #aces have a value of 1 or 11
    # so it is possible for a hand to have more than 1
    #value
    #Examples: ['8', '7'] -> [15]
    #['Q', '6'] -> [16]
    #['Q', 'A'] -> [11, 21]

myDeck = getDeckOfCards()
shuffleDeck(myDeck)
hand1 = dealABlackJackHand(myDeck)
hand2 = dealABlackJackHand(myDeck)
print(hand1)
print(hand2)
print(myDeck)
answer = "2 3 4 5 6 7 8 9 10 J Q K A Joker".split()
print(answer)
"""

#My Code:
def getValueOfBlackJackHand(hand):
  finalvalue = []
  value1 = 0
  value2 = 0
  value3 = 0
  value4 = 0
  tenvars = "JKQ"
  for handPos in range (0, len(hand)):
    if hand[handPos] == "A":
      if value1 == 11:
        value3 = 12
        value4 = 12
      value1 = value1 + 11
      value2 = value2 + 1
    for tenvarsPos in range(len(tenvars)-1,-1,-1):
      if hand[handPos] == tenvars[tenvarsPos]:
        if value1 == 11:
          value1 = value1 + 10
          value2 = value2 + 10
        else: value1 = value1 + 10
      elif hand[handPos] != tenvars[tenvarsPos]:
        if hand[handPos] != "A":
          if value1 == 11:
            value1 = value1 + int(hand[handPos])
            value2 = value2 + int(hand[handPos])
          else: value1 = value1 + int(hand[handPos])
  if 21 >= value1 > value2:
    finalvalue.append(value1)
  elif 21 >= value2 > value3:
    finalvalue.append(value2)
  elif 21 >= value3 > value4:
    finalvalue.append(value3)
  elif 21 >= value4 > 0:
    finalvalue.append(value4)
  return finalvalue

my_hand = ['A','Q']
answer = getValueOfBlackJackHand(my_hand)
print(answer)
