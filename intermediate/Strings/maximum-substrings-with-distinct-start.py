# 3760. Maximum Substrings With Distinct Start - Medium
class Solution:
    def maxDistinct(self, s: str) -> int:
        hset = set()
        for ch in s:
            hset.add(ch)
            
        return len(hset)
