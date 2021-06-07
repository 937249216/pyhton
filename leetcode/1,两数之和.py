class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(n+1):
                if nums[i]+nums[j] == target:
                    return[i,j]
        return[]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:  
        hashtable = dict()
        for i,num in enumerate(nums):
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]]==i
        return[]    