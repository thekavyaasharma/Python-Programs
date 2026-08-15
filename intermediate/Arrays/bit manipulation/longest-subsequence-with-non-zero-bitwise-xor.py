# 3702. Longest Subsequence With Non-Zero Bitwise XOR - Medium
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if all(x==0 for x in nums):
            return 0
        res = len(nums)
        temp = 0 
        for i in nums:
            temp^=i
        if temp == 0:
            return res-1
        return res
