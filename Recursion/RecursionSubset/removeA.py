def skip(p,up):
    up=list(up)
    if len(up)==0:

        return p
    ch=up[0]
    if ch=="a":

        return skip(p,up[1:])
    else:
        return skip(p+ch,up[1:])



print(skip("","wearxa"))

