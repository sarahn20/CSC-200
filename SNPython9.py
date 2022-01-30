#Assignment Description:
"""
Expand the current program to allow a single player to play a blackjack hand.  The player should initially be dealt 2 cards, 
then their hand should be displayed to them along with its current best value.  The user should be able to either "hit" and 
get another card or "stay" where the final state of their hand is displayed along with its value.  A Player may only "hit" as 
long as they have not gone over 21.  Once their hand exceeds 21, the program stops asking if they want another card and shows 
the final state of their hand.
"""

#Code give from class:
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
    cardVals = splitCommaDelimStringToList("2,3,4,5,6,7,8,9,10,J,Q,K,A")
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
#['2','K','A','A']
def countAcesInHand(hand):
    count = 0
    for i in range(0, len(hand)):
        if(hand[i] == 'A'):
            count = count + 1
    return count
def convertCardToValue(cardString):
    if(cardString == 'J'):
        return 10
    elif(cardString == 'Q'):
        return 10
    elif(cardString == 'K'):
        return 10
    elif(cardString == 'A'):
        return 1
    else:
        return int(cardString)
def getValueOfBlackJackHand(hand):
    number_of_aces = countAcesInHand(hand)
    currentHandValue = 0
    for cardString in hand:
        currentHandValue = currentHandValue + convertCardToValue(cardString)
    #we now have the minimum value our hand is worth, aces might make a diff
    for i in range(0, number_of_aces):
        if(currentHandValue + 10 <= 21):
            currentHandValue = currentHandValue + 10
    return currentHandValue

myDeck = getDeckOfCards()
shuffleDeck(myDeck)
hand1 = dealABlackJackHand(myDeck)
hand2 = dealABlackJackHand(myDeck)
print(getValueOfBlackJackHand(['2','K']))
print(getValueOfBlackJackHand(['2','K','A']))
print(getValueOfBlackJackHand(['2','8','A']))
"""
#My Code:

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
    cardVals = splitCommaDelimStringToList("2,3,4,5,6,7,8,9,10,J,Q,K,A")
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
#['2','K','A','A']
def countAcesInHand(hand):
    count = 0
    for i in range(0, len(hand)):
        if(hand[i] == 'A'):
            count = count + 1
    return count
def convertCardToValue(cardString):
    if(cardString == 'J'):
        return 10
    elif(cardString == 'Q'):
        return 10
    elif(cardString == 'K'):
        return 10
    elif(cardString == 'A'):
        return 1
    else:
        return int(cardString)
def getValueOfBlackJackHand(hand):
    number_of_aces = countAcesInHand(hand)
    currentHandValue = 0
    for cardString in hand:
        currentHandValue = currentHandValue + convertCardToValue(cardString)
    #we now have the minimum value our hand is worth, aces might make a diff
    for i in range(0, number_of_aces):
        if(currentHandValue + 10 <= 21):
            currentHandValue = currentHandValue + 10
    return currentHandValue

myDeck = getDeckOfCards()
shuffleDeck(myDeck)

#Deal player two cards
currenthand = dealABlackJackHand(myDeck)
print("Your current hand is: ", currenthand)
print("The best current value of your hand is: ", getValueOfBlackJackHand(currenthand))
# If currenthand value is still under 21
while (getValueOfBlackJackHand(currenthand)) < 21:
  response = input("Would you like to hit or stay? ")
  if response == "hit":
    newCard = splitCommaDelimStringToList(dealCard(myDeck))
    currenthand = currenthand + newCard
    if (getValueOfBlackJackHand(currenthand)) < 21:
      print("Your current hand is: ", currenthand)
      print("The best current value of your hand is: ", getValueOfBlackJackHand(currenthand))
    newCard = None
  if response == "stay":
    print("Your final hand is: ", currenthand)
    print("The final value of your hand is: ",(getValueOfBlackJackHand(currenthand)))
    break 
if (getValueOfBlackJackHand(currenthand)) >= 21:
    print("Your final hand is: ", currenthand)
    print("The final value of your hand is: ",(getValueOfBlackJackHand(currenthand)))
    
        
