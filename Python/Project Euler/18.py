def splitMaxPath(length):
    stringPyramid = []
    intPyramid = []
    for level in range(length):
        layer = input()
        stringPyramid.append(layer)
    for x in stringPyramid:
        intPyramid.append(x.split(" "))
    return intPyramid
  
def findMaxPath(pyramid,length):
    twoBehind = length - 2
    oneBehind = length - 1
    for x in range(len(pyramid)):
        for y in range(len(pyramid[twoBehind-x])):
            if twoBehind - x > -1:
                currentVar = int(pyramid[twoBehind-x][y])
                lowerLevelVarOne = int(pyramid[oneBehind-x][y])
                lowerLevelVarTwo = int(pyramid[oneBehind-x][y+1])
                if currentVar + lowerLevelVarOne > currentVar + lowerLevelVarTwo or currentVar + lowerLevelVarOne == currentVar + lowerLevelVarTwo:
                    pyramid[twoBehind-x][y] = (currentVar + lowerLevelVarOne)
                elif currentVar + lowerLevelVarOne < currentVar + lowerLevelVarTwo:
                    pyramid[twoBehind-x][y] = (currentVar + lowerLevelVarTwo)
    return pyramid[0][0]
            
length = int(input("How tall is the pyramid?: "))
pyramid = splitMaxPath(length)
print(findMaxPath(pyramid,length))
k = input("END")
