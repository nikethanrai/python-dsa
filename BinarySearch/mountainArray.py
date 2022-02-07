
def mountainArray(arr):
    N = len(arr)
    low = 0
    high = N - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] > arr[mid+1]:
            high = mid-1
        else:
            low = mid + 1
    return (high)


print(mountainArray([1, 4, 6, 7, 90]))

