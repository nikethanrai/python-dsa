def dice(Num):
    return subset("",Num,[])
def subset(p,target,x):
    if target==0:
        x.append(p)
        return

    for i in ( i for i in range(1,target+1) if i<=6):
        subset(p+str(i),target-i,x)
    return x
print(dice(7))