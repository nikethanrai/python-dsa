def binary(arr,Num):
    N= len(arr)
    low=0
    high=N-1
    ans=0
    
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==Num:
            return(arr[mid])


        if arr[mid]>Num:
            high=mid-1
        else:
            ans = arr[mid]
            low=mid+1
    return (ans)
print(binary([1,4,6,7,9,10],5))

