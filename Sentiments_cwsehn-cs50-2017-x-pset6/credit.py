# check for valid input from user...
num = -1 
while num < 0:
    try:
        num = int(input("Number: "))
    except ValueError:
       print("Retry...")
       
numStr = str(num)
numList = []
cardLen = len(numStr)
digits = 0

# create reverse order list of digits from cardNum.....
while digits < cardLen:
    digit = num % 10
    numList.append(digit)
    digits += 1
    num -= digit
    num = int(num/10)
    
# function to test Luhn's algorithm
def checkSum(numList):
    index = 0
    checkNum = 0
    while index < len(numList):
        if index % 2 == 0:
            checkNum += numList[index]
        elif numList[index] < 5:
            checkNum += numList[index] * 2
        else:
            tempSum = numList[index] * 2
            tempSum = (tempSum % 10) + 1
            checkNum += tempSum
        index += 1
        
    if checkNum % 10 == 0:
        return True
    else:
        return False
        

# function to test card company IDs
def cardCheck(numList):
    cardLen = len(numList)
    
    if (cardLen == 15) and ((numList[14] == 3) and (numList[13] == 4 or numList[13] == 7)):
            return "AMEX"

    elif ((cardLen == 16 and numList[15] == 4) or (cardLen == 13 and numList[12] == 4)):
        return "VISA"
    
    elif (cardLen == 16) and ((numList[15] == 5) and (numList[14] > 0 and numList[14] < 6)):
            return "MASTERCARD"
            
    else:
       return "INVALID"
       
# call validity check functions ...print result...        
validCheck = checkSum(numList)

if validCheck:
    print(cardCheck(numList))      
else:
    print("INVALID")
