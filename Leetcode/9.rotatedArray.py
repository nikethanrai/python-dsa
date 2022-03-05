def rotatedArr(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid= high+(low-high)//2
        if arr[mid]==target:
            return mid
        if arr[mid]>=arr[low]:
            if arr[mid]>target>arr[low]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:high=mid-1
print(rotatedArr( [7,8,0,1,2,3,4,5],5))

def pivot(arr):
    low = 0
    high = len(arr) - 1
    while low <=high:
        mid = high + (low - high) // 2
        if mid<len(arr)-1 and arr[mid]>arr[mid+1]:
            return mid
        if arr[mid]<arr[low]:
            high=mid-1
        else:low=mid+1
    return (len(arr)-1)




print(pivot ([7,8,9,10,11,121]))

