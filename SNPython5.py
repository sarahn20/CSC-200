#Assignment Description: Make baseToDecimalConverter work for bases up to base 37

#Code given from class:
"""
def baseToDecimalConverter(value, base):
  place = 1
  sum = 0
  for currPosInString in range(len(value)-1, -1, -1):
    sum = sum + (int(value[currPosInString]) * place)
    place = place * base
  return sum

answer = baseToDecimalConverter("1010101010", 2)
print(answer)
print(baseToDecimalConverter("12456", 8))
"""

#My Code:

def baseToDecimalConverter(value, base):
  place = 1
  sum = 0
  basalMultiplier = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for currPosInString in range(len(value)-1, -1, -1):
    for currPosinbasalMultiplier in range(0,len(basalMultiplier)):
      if(value[currPosInString] == basalMultiplier[currPosinbasalMultiplier]):
        sum = sum + (currPosinbasalMultiplier * place)
    place = place * base
  return sum
answer = baseToDecimalConverter("3MI9F0W6", 37)
print(answer)


  
