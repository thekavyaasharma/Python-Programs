# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray - Easy
class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) == 1:
            return 1
        
        stk = [-1]
        stk2 = [float('inf')]
        x = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > stk[-1]:
                stk.append(nums[i])
            else:
                stk = [-1]
                stk.append(nums[i])
            if nums[i] < stk2[-1]:
                stk2.append(nums[i])
            else:
                stk2 = [-1]
                stk2.append(nums[i])
            x = max(x, len(stk2)-1, len(stk)-1)
        
        return x
