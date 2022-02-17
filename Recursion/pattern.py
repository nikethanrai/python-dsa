def pattern(r,c):
    if r==0:
        return ("")
    if r>c:
        print("*")
        return pattern(r,c+1)
    else:
        print("\n")
        return(pattern(r-1,0))
print(pattern(4,0))

