def RBS(arr,target):
    pivot=findPivot(arr)


    if pivot==-1:
        return binarySearch(arr,target,0,len(arr-1))
    if arr[pivot]==target:
        return pivot
    if target>arr[0]:
        return binarySearch(arr,target,0,pivot-1)
    else:return binarySearch(arr,target,pivot+1,len(arr)-1)



def binarySearch(arr,target,start,end):
    while end>=start:
        mid=start+(end-start)//2
        if arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1
        else:
            return mid
    return -1

def findPivot(arr):
    start=0
    end=len(arr)-1

    while start<=end:
        mid = start + (end - start) // 2
        if mid<end and arr[mid]>arr[mid+1]:
            return mid
        if arr[mid]<arr[mid-1]:
            return mid-1
        if arr[mid]<=arr[start]:
            end=mid-1
        else:
            start=mid+1
    return -1



print(RBS([1],0))