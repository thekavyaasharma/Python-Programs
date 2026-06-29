# 217 - Contains Duplicates - Easy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[i-1]:
                return True
                break
        return False
