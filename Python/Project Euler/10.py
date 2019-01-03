
m = int(input("Prime Limit: "))

def Prime_Sum(m):
    primes = [2]
    prime_sum = 2
    for x in range(3,m,2):
        for prime in primes:
            if x % prime == 0:
                break
        else:
            primes.append(x)
            prime_sum += x
            print(x)
    return("Sum: " + str(prime_sum))
            

if __name__ == "__main__":
    print(Prime_Sum(m))
    k = input("END")
    quit()
