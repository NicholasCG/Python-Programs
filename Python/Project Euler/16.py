
power = int(input("To what power?: "))
twotothousand = str(2**power)
powerSum = 0
for x in twotothousand:
    powerSum += int(x)
print("Digit sum: " + str(powerSum))
k = input("END")