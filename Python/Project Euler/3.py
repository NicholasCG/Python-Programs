num = 600851475143
divis = []
mult = 1
for x in range(1, num):
    if num % x == 0:
        print(x)
        divis.append(x)
        mult = mult * x
    if mult == num:
        break
k = input("END")
