limit = int(input("Input a limit for the collatz odd numbers: "))
for x in range(1,limit,2):
    end = 3*x + 1
    while (end % 2 == 0):
        end = end/2
    print(("{:3d} : {:3d}").format(x,int(end)))
    
k = input("END")