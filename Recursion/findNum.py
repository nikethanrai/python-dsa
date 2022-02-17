def findNum(arr,N):

    return helper(arr,N,0,0)
a=[]
def helper(arr,N,i,x):

    if i==len(arr)-1:
        if arr[i]==N:
            a.append(i)
            return (x+1,a)
        else:
            return (x,a)

    if arr[i]==N:
        a.append(i)
        return helper(arr,N,i+1,x+1)
    else:
        return helper(arr,N,i+1,x)

print (findNum([2,1,4,6,4,4,4,4],4))


