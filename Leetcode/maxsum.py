def maxSum(arr,k):
    if len(arr)<k:
        return
    max_sum=0
    current=sum(arr[:k])

    for i in range(len(arr)-k):
        current=current-arr[i]+arr[i+k]
        max_sum=max(max_sum,current)
    return max_sum



print(maxSum([1, 4, 2, 10, 2,3, 1, 0, 20],4))