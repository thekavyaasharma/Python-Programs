#424. Longest Repeating Character Replacement - Medium
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = dict()
        i = 0
        res = 0
        n = len(s)
        for j in range(n):
            d[s[j]] = 1 + d.get(s[j],0)
            maxFreq = max(d.values())
            curLen = j-i+1
            if curLen - maxFreq > k:
                d[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res
        
        