def cyclicSort(arr):
    i=0
    while i< len(arr):
        correct=arr[i]
        if (arr[i]<len(arr) and arr[i]!=arr[correct]):
            swap(arr,i,correct)
        else:
            i+=1
    for i in range(len(arr)):
        if(arr[i]!=i):
            return i
    return len(arr)

def swap(arr,i,correct):
    temp=arr[i]
    arr[i]=arr[correct]
    arr[correct]=temp

print(cyclicSort([4,3,1,0]))
