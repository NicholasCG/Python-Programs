latticeList = []
limit = int(input("Input grid size limit: ")) + 1
for x in range(limit):
    latticeList.append([])
    latticeList[x].append(1)
    latticeList[0].append(1)
latticeList[0].pop()
for x in range(1,limit):
    for y in range(1,limit):
        latticeList[x].append(latticeList[x-1][y] + latticeList[x][y-1])
print("End # of lattice paths: " + str(latticeList[limit-1][limit-1]))
k = input("END")
