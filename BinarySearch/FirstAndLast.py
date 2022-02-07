def FirstAndLast(arr, Num, value):
    N = len(arr)
    low = 0
    high = N - 1
    pos = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == Num:
            pos = mid
            if (value):
                high = mid - 1
            else:
                low = mid + 1

        elif arr[mid] > Num:
            high = mid - 1
        else:
            low = mid + 1
    return (pos)


ans = [-1, -1]
arr = [1, 1, 1, 1, 4, 4, 4, 5, 5, 5, 7]
Num = 7
ans[0] = FirstAndLast(arr, Num, True)
if ans[0] != -1:
    ans[1] = FirstAndLast(arr, Num, False)
print(ans)
