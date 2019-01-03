def addSum(count):
    sums = 0
    for x in range(1, count + 1):
        currentNum = int(input())
        sums += currentNum
    return sums
def printDigitLen(length,sums):
    return str(sums)[:length]
    
firstSum = int(input("Length of added numbers: "))
newSum = addSum(firstSum)
print(newSum)
print(printDigitLen(10,newSum))
k = input("END")
    
