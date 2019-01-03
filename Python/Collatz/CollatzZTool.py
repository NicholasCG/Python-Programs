existing_numbers = []
current = 1
limit = int(input("Set the upper limit for what first iterations you want to find: "))
nots = int(input("Do you want to find all first cases (0), or all not-first cases? (1): "))

while (current <= limit):
    end = 3*current + 1
    while (end % 2 == 0):
        end = end/2

    #print (end in existing_numbers)
        
    if not (end in existing_numbers) and nots == 0:
        print(("{:3d} is the first to go to {:3d}").format(current,int(end)))
        existing_numbers.append(end)
    elif (end in existing_numbers) and nots == 1:
        print(("{:3d} is not the first to go to {:3d}").format(current,int(end)))
        exit
    else:
        existing_numbers.append(end)
        
    current += 2
    
k = input("END")
