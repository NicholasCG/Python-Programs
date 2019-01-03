tempsum = 0
fibnum = 1
newfibnum = 2
evensum = 0
limit = int(input("Limit of Sequence: "))
while newfibnum < limit:
    print(fibnum, newfibnum)
    tempsum = fibnum + newfibnum
    fibnum = newfibnum
    newfibnum = tempsum
    if fibnum % 2 == 0:
        evensum += fibnum
print("Sum: " + str(evensum))
k = input("END")