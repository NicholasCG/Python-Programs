max = [0,0]
for x in range(1000000):
    chainLen = 1
    n = x
    while n > 1:
        chainLen += 1
        if n % 2 == 0:
            n = n / 2   
        else:
            n = 3*n + 1            
    if chainLen > max[0]:
       max[0] = chainLen
       max[1] = x
print("found %s at length %s" % (max[1],max[0]))
k = input("END")
