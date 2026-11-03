# 3736. Minimum Moves to Equal Array Elements III - Easy
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = float('-inf')
        for i in nums:
            if i > mx:
                mx = i
        return sum([mx-i for i in nums])

        