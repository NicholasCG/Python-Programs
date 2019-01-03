stdin = int(input("What do you want the sum of a, b, and c to be?: "))

def Pythagorian_Triplet(stdin):
    for a in range(1,stdin):
        for b in range(a+1, a + stdin):
            c = stdin - a - b
            if a**2 + b**2 == c**2:
                return("a: {0}, b: {1}, c: {2} \nProduct: {3}".format(a, b, c, a*b*c))
    else:
        return("Sorry, there are no possible matches.")

if __name__ == "__main__":
    print(Pythagorian_Triplet(stdin))
    k = input("END")
    quit()