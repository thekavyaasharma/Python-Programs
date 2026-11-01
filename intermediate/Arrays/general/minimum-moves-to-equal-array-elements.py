# 453. Minimum Moves to Equal Array Elements - Medium
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = float('inf')
        for i in nums:
            if i < mn:
                mn = i
        mov = 0
        for x in nums:
            mov += x-mn
        return mov