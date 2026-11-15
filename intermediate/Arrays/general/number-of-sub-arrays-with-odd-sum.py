# 1524. Number of Sub-arrays With Odd Sum - Medium
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        even = 1
        odd = 0
        s = 0
        m = 10**9+7
        for i in arr:
            s = (s+i)%2
            if s== 1:
                ans = (ans+even)%m
                odd+=1
            else:
                ans = (ans+odd)%m
                even+=1
        return ans
        