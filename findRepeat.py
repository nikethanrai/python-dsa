def cyclicSort(arr):
    i=0
    miss=[]
    while i< len(arr):
        correct=arr[i]-1
        if arr[i]!=arr[correct]:
            swap(arr,i,correct)
        else:
            i+=1
    j=0
    while j<len(arr):
        if arr[j]!=j+1:
            miss.append(arr[j])
        j+=1

    return miss
def swap(arr,i,correct):
    temp=arr[i]
    arr[i]=arr[correct]
    arr[correct]=temp
print (cyclicSort([1,1,2,3]))
