
def steps(N):
    return helper(N,0)
def helper(n,c):
    if n==0:
        return c-1
    if n%2!=0:
        return helper((n-1)/2,c+2)
    else:
        return helper(n/2,c+1)
print(steps(16))
