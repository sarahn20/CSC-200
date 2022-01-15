#Assignment Description: 
"""
using the code from slack as a starting point, write a program that stores the number of pennies in a variable and then displays to the screen the best way to give change in terms of dollar bills, quarters, dimes, nickels, and pennies.
So if the variable held 128 pennies, then your output should be:
dollars: 1
quarters: 1
dimes: 0
nickels: 0
pennies: 3
"""

#Code given from class (not Slack):
"""
#Variables
numberofPennies = 1013
numberOfDollars = numberOfPennies // 100
numberOfPennies = numberOfPennies % 100
#print out the best way of giving change where
#our highest amount is 1 dollar bills

print(fname)
print(lname)
print(age)
print(fname + " " + lname)


if(age >= 18):
  print("Get some smokes")
  if(age >= 21):
    print("Hit the bar")
"""

#My Code:
#Variables
numberOfPennies = 128
numberOfDollars = numberOfPennies // 100
numberOfPennies = numberOfPennies % 100
numberOfQuarters = numberOfPennies // 25
numberOfPennies = numberOfPennies % 25
numberOfDimes = numberOfPennies // 10
numberOfPennies = numberOfPennies % 10
numberOfNickels = numberOfPennies // 5
numberOfPennies = numberOfPennies % 5

print("dollars:" , numberOfDollars)
print("quarters:" , numberOfQuarters)
print("dimes:" , numberOfDimes)
print("nickels:" , numberOfNickels)
print("pennies:" , numberOfPennies)
