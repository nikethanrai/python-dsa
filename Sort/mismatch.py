class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(arr):
            correct = arr[i] - 1
            if arr[i] != arr[correct]:
                swap(arr, i, correct)
            else:
                i += 1
        j = 0
        while j < len(arr):
            if arr[j] != j + 1:
                rep = (arr[j])
                val = j + 1
            j += 1

        return ([rep, val])

def swap(arr,i,correct):
    temp=arr[i]
    arr[i]=arr[correct]
    arr[correct]=temp


