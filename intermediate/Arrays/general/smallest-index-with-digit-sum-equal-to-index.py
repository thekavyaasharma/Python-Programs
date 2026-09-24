# 3550. Smallest Index With Digit Sum Equal to Index - Easy
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            temp = 0
            while nums[i] > 0:
                temp += nums[i]%10
                nums[i]//=10
            if temp == i:
                return i
        return -1

        