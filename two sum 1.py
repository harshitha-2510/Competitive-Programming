class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[]

"""
store={}
for i,ele in enumerate(nums):
    if target-ele in store:
        return [store[target-ele],i]
    else:
        store[ele]=i
"""
