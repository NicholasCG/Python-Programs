
m = int(input("Nth Prime: "))

def Nth_Prime(m):
    primes = [2]
    primecount = 1
    if m == 1:
        print("1")
    for x in range(3,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,2):
        for prime in primes:
            if x % prime == 0:
                break
        else:
            primes.append(x)
            primecount += 1
        if primecount == m:
            return x
            

if __name__ == "__main__":
    print(Nth_Prime(m))
    k = input("END")
    quit()
