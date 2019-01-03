def findAmicable(n, m):
    p = (2**(n-m) + 1) * 2**m - 1
    q = (2**(n-m) + 1) * 2**n - 1
    r = (2**(n-m) + 1)**2*2**(m+n)-1
    print(p)
    print(q)
    print(r)
findAmicable(4,5)
k = input("N")