
def combinationSum(arr,target):


    res =helper(arr,target,0,[],[])
    return res
def helper(arr,target,index,p,x):
    if target<0:
        return
    if target==0:
        x.append(p)
        return
    for i in range(index,len(arr)):
        helper(arr,target-arr[i],i,p+[arr[i]],x)
    return x
print(combinationSum([1,3],4))
