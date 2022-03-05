
def searchInsertPos(arr,target):
    if arr==[]:
        return 0
    low=0
    high=len(arr)-1
    while low<=high:
        mid=high+(low-high)//2
        if arr[mid]==target:
            return mid
        if arr[mid]>target:
            high=mid-1
        else:low=mid+1
    return low
print(searchInsertPos([2,3,4,6,8],0))
