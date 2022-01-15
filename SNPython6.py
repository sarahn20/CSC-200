#Assignment Description: 
"""
For this assignment you can’t use int()
Write the int function that takes a string representation of a base 10 number as a parameter and returns the decimal equivalent.
“123” -> 123
“456” -> 456
"""


#My Code:
def my_int(value, base):
  place = 1
  sum = 0
  basalMultiplier = "0123456789"
  for currPosInString in range(len(value)-1,-1,-1):
    for currPosinbasalMultiplier in range(0,len(basalMultiplier)):
      if(value[currPosInString] == basalMultiplier[currPosInBasalMultiplier]):
        sum = sum + (currPosinbasalMultiplier * place)
    place = place * base
  return sum
answer = my_int("123", 10)
print(answer)
#Can see output is an int because it can work in mathematical expressions:
print(answer + 2)
                                          
