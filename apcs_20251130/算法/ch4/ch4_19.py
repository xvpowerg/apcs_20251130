def gcd_iter(m,n):
    while n!=0:
        print(f"gcd({m},{n})",end="")
        r = m % n
        m = n
        n = r
    return m    
def gcd_rec(m,n):
    print(f"gcd({m},{n})",end="")
    if n ==0:
        return m
    else:
        return gcd_rec(n,m%n)
n1 = int(input("n1"))
n2 = int(input("n2"))

if n1<n2:
    n1,n2 = n2,n1

gcd = gcd_iter(n1,n2)
print(gcd)
gcd = gcd_rec(n1,n2)
print(gcd)

