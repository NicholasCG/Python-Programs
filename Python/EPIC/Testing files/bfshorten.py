commandtype = []
commandnum = []
currentcommand = ""
k = input("Choose run: ")
for x in k:
    if x in ['<','>','+','-',',','.','[',']']:
        if x != currentcommand:
            currentcommand = x
            commandtype.append(x)
            commandnum.append(1)
        else:
            if x == "[" or x == "]":
                commandtype.append(x)
                commandnum.append(1)
                continue
            commandnum[len(commandnum)-1] += 1
for x in commandtype:
    print(x + " ",end = "")
print(" ")
for y in commandnum:
    print(str(y) + " ",end = "")
print("\n")
k = input("END")
