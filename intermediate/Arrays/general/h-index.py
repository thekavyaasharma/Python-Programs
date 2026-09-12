# 274. H-Index - Medium
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()

        for i in range(n):
            if n-i <= citations[i]:
                return n-i
        return 0
        
class Solution(object):
    def hIndex(self, c):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(c)
        c.sort()
        high = n-1
        low = 0
        ans = 0
        while low <= high:
            mid = low + (high-low)//2
            if n-mid <= c[mid]:
                ans =  n- mid
                high = mid-1
            else:
                low = mid+1
        return ans