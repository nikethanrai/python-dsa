def comb(s):
    x=[]
    for i in range(len(s)):
        x.append(s[len(s)-i-1])
    print(*x,sep="")
comb("Hello")

