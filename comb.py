def com(n,r):
    if n==r or r==0:
        return 1
    else:
        return com(n-1,r)+com(n-1,r-1) #n+1Cr= nCr-1+nCr
    
a=input("Enter n, r :").split()

print(a[0]+'C'+a[1], "is: ", com(int(a[0]),int(a[1])))