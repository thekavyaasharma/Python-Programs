# 3904. Smallest Stable Index II - Medium
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        minval = [None] * n
        minval[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            minval[i] = min(nums[i],minval[i+1])

        maxval = 0
        for i in range(n):
            maxval = max(nums[i],maxval)
            if maxval - minval[i] <= k:
                return i
                break
        return -1
        