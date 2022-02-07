def cyclicSort(arr):
    i=0
    while i< len(arr):
        correct=arr[i]-1
        if arr[i]!=arr[correct]:
            swap(arr,i,correct)
        else:
            i+=1
    print(arr)
def swap(arr,i,correct):
    temp=arr[i]
    arr[i]=arr[correct]
    arr[correct]=temp
cyclicSort([4,3,2,1,7,7,6])
