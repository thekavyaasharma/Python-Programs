# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum - Easy
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        n = len(nums)
        s = set(nums)

        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                total+=nums[i]
            else:
                break
        
        while total in s:
            total+=1
        return total
        