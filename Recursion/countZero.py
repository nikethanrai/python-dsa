def countZero(N):
    return helper(N,0)

def helper(n,c):
    if n==0:
        return c
    if n%10==0:
        return helper(n//10,c+1)
    else:
        return helper(n//10,c)

print(countZero(50809))




