
def twoSum(nums,target):
    dict={}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]],i]
        else:
            dict[target-nums[i]]=i

print(twoSum([2,3,4,1,3,5,3,2],9))


