# 75. Sort Colors - Medium
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        idx = 0
        for i in range(3):
            freq = d[i]
            nums[idx : idx+freq] = [i] * freq
            idx += freq