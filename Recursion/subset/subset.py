x=[]
def subset(p,up):
    if len(up)==0:
        if p!="":
            
            x.append(p)
        return


    ch = up[0]
    subset(p+ch,up[1:])
    subset(p,up[1:])
    return x


print(subset("","123"))