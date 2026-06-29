# 283. Move Zeroes - Easy
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        n = len(nums)

        for right in range(n):
            if nums[right] != 0:
                if right != left:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp
                left +=1
        


        