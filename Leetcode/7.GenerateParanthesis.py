def genPara(n):
    return helper(n,n,"",[])

def helper(open,close,p,x):
    if open==0 and close==0:
        x.append(p)
        return x
    if open>0:
        helper(open-1,close,p+"(",x)
    if open<close:
        helper(open,close-1,p+")",x)
    return x
print(genPara(3))

