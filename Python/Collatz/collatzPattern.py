x = 25
while (x < 1000000):
    num = (x-1) / 3

    if num - int(num) == 0:
        print ( str(x) + " : " + str((x-1) / 3))
    x = 2 * x
k = input("END")