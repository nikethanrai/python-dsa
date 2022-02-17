def sumOfDigits(N):
    if N//10==0:
        return N
    return (N%10)+sumOfDigits(N//10)

print(sumOfDigits(1231))