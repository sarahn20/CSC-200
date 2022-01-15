#Assignment Description: write a program that prompts the user for a number of seconds and prints to the screen the number of years, days, hours, minutes, and seconds that is equivalent to.

#My Code:

print("The number of seconds you input will be converted to the equivalent number of years, days, hours, minutes, and seconds.")
NumberOfSeconds = int(input("Please input a certain number of seconds:"))
# Variables
NumberofYears = NumberofSeconds // (60*60*24*365)
NumberofSeconds = NumberofSeconds % (60*60*24*365)
NumberofDays = NumberofSeconds // (60*60*24)
NumberofSeconds = NumberofSeconds % (60*60*24)
NumberofHours = NumberofSeconds // (60*60)
NumberofSeconds = NumberofSeconds % (60*60)
NumberofMinutes = NumberofSeconds // (60)
NumberofSeconds = NumberofSeconds % (60)
# Print Statements
print("Years:",NumberofYears)
print("Days:",NumberofDays)
print("Hours:",NumberofHours)
print("Minutes:",NumberofMinutes)
print("Seconds:",NumberofSeconds)
