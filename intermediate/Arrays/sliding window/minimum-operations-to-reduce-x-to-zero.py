# 1658. Minimum Operations to Reduce X to Zero - Medium
class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        k = sum(nums)  - x
        if k < 0:
            return -1
       

        best , s , i = -1,0,0
        n = len(nums)
        for j in range(n):
            s+= nums[j]

            while s > k:
                s-= nums[i]
                i+=1

            if s == k:
                best = max(best, j-i+1)

        return -1 if best < 0 else n-best 
        