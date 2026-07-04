# 3925. Concatenate Array With Reverse - Easy
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [] * (2*n)
        ans[:n] = nums
        ans[n:] = nums[::-1]
        return ans
        