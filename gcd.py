c=int(input("Enter first integer:"))
d=int(input("Enter Second integer:"))

def gcd(a,b):
    while a%b !=0:
        t,b=b,a%b
        a=t
    return b
print("GCD of",c,d, "is ",gcd(c,d))
print("LCM of",c,d, "is",(c*d)//gcd(c,d))


