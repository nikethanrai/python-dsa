def stringCeiling(arr, Num):
    N = len(arr)
    low = 0
    high = N - 1
    ans = 0
    if Num>=arr[-1]:
        return arr[0]

    while low <= high:
        mid = low + (high - low) // 2


        if arr[mid] > Num:
            ans = arr[mid]
            high = mid - 1
        else:

            low = mid + 1
    return (ans)


print(stringCeiling(["m", "n", "o", "q"], "m"))

