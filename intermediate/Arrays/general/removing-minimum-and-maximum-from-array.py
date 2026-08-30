# 2091. Removing Minimum and Maximum From Array - Medium
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        left = min(nums.index(min(nums)), nums.index(max(nums)))
        right = max(nums.index(min(nums)), nums.index(max(nums)))

        n = len(nums)

        front = right +1
        back = n - left

        both = (left + 1) + (n - right)

        return min(front, back,both)