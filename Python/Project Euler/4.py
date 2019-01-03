rangenum = list(range(10000,998001))
for x in rangenum[::-1]:
    x = str(x)
    if x == x[::-1]:
        x = int(x)
        for y in range(100,1000):
            if x % y == 0 and x / y < 1000:
                print(x)
                k = input("END")
                exit()