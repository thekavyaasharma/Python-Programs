# 3644. Maximum K to Sort a Permutation - Medium
class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = -1
        for i,v in enumerate(nums):
            if i!= v:
                k = k & v
            if not k :
                return 0
        return max(k,0)
        