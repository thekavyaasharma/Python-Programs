# 3498. Reverse Degree of a String - Easy
class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        for i in range(n):
            res += (26-(ord(s[i])-ord('a'))) * (i+1)

        return res
        
        