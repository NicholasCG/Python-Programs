#@author Nicholas Gray
#@version 8/21/17

"""First test is to create a triangle number/
    Second is to test for its divisors.
    Third is to find if it is bigger than the minimum requirement of divisors.
    Fourth is optimization"""
    
def highDivisTriangleNum(divisor):
    divisorNum = 0
    triangleNum = 1
    currentCount = 1
    while divisorNum < divisor:
      for x in range(1,triangleNum + 1):
        if triangleNum % x == 0 and triangleNum/x > x:
          divisorNum += 2
        elif triangleNum % x == 0 and triangleNum/x == x:
          divisorNum += 1
        elif triangleNum % x == 0 and triangleNum/x < x:
          break
      if divisorNum > divisor:
        return triangleNum
      else:
        currentCount += 1
        triangleNum += currentCount
        divisorNum = 0
            
    
    
divisor = int(input("Minimum # of Divisors: "))
print(highDivisTriangleNum(divisor))
k = input("END")
