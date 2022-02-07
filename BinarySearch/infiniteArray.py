def binary(arr, low, high, Num):
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == Num:
            ans = mid
            return (ans)
        elif arr[mid] > Num:
            high = mid - 1
        else:
            low = mid + 1
    return (ans)


def infiniteArray(arr, Num):
    start = 0
    end = 1
    while Num >arr[end]:
        temp = end + 1
        end = end + (end - start + 1) * 2
        start = temp
    return binary(arr, start, end, Num)


print(infiniteArray([1,3,5,6,9,99,100,101,201,202,203,204,205,206,500,4599],202))