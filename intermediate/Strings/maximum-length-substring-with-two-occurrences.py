# 3090. Maximum Length Substring With Two Occurrences - Easy
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # sliding window approach 
        res = l = 0
        freq = defaultdict(int)
        for right in range(len(s)):
            i = s[right]
            freq[i] +=1
            while freq[i] > 2:
                freq[s[l]]-=1
                l+=1 
            res=max(res,right-l+1)
        return res