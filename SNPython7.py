#Assignment Description: 
"""
write a function the does the math contained within a string.  Assuming only addition and subtraction are supported and there are no spaces.

For example "123+8-2+111" would output, 240
"""

#My Code:

def processExpression(expr):
    currNum = ""
    prevNum = ""
    Op = ""
    for currStringPos in range(0,len(expr)):
        if expr[currStringPos] == "+":
            if Op == "+":
                prevNum = (int(prevNum) + int(currNum))
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "-":
                prevNum = int(prevNum) - int(currNum)
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "":
                Op = Op + expr[currStringPos]
                prevNum = currNum
                currNum = ""
        if expr[currStringPos] == "-":
            if Op == "+":
                prevNum = (int(prevNum) + int(currNum))
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "-":
                prevNum = int(prevNum) - int(currNum)
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "":
                Op = Op + expr[currStringPos]
                prevNum = currNum
                currNum = ""
        if expr[currStringPos].find("+") == -1:
            if expr[currStringPos].find("-") == -1:
                currNum = currNum + expr[currStringPos]
        if currStringPos == len(expr)-1:
            if Op == "+":
                prevNum = int(prevNum) + int(currNum)
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "-":
                prevNum = int(prevNum) - int(currNum)
                prevNum = str(prevNum)
                currNum = ""
                Op = expr[currStringPos]
            elif Op == "":
                Op = Op + expr[currStringPos]
                prevNum = currNum
                currNum = ""
    return prevNum
expr = "123+8-2+111"
answer = processExpression(expr)
print(answer)
