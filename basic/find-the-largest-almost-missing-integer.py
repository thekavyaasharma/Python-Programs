# 3471. Find the Largest Almost Missing Integer - Easy
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == n:
            return max(nums)
            
        elif k == 1:
            s = sorted(nums)
            for i in range(n-1,-1,-1):
                if nums.count(s[i])==1:
                    return s[i]
                    break
            else:
                return -1

        elif 1 < k < n:
            if nums.count(nums[0]) == 1 and nums.count(nums[-1]) ==1:
                return max(nums[0], nums[-1])
            elif nums.count(nums[0]) > 1 and nums.count(nums[-1]) > 1:
                return -1
            else:
                return nums[0] if nums.count(nums[0]) < nums.count(nums[-1]) else nums[-1]
        