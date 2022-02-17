def bubbleSort(arr):
    i=0
    swapped=False

    while i<len(arr):
        for j in range(1,len(arr)-i):
            if arr[j]<arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
                swapped=True
        if (not swapped):
            break;


        i+=1

    return(arr)
print(bubbleSort([1,2,3,4]))




