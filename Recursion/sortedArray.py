def sorted(arr):
    return helper(arr,0)
def helper(arr,i):
    if (len(arr)-1)==i:
        return True
    return arr[i]<arr[i+1] and helper(arr,i+1)
print(sorted([4,6,11,10]))