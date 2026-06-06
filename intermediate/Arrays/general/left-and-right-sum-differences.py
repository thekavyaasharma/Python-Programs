# 2574 EASY
class Solution :
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        rightSum = 0
        n = len(nums)
        for i in range(n):
            rightSum += nums[i]
        
        leftSum = 0
        ans = [None] * n 

        for i in range(n):
            rightSum -= nums[i]

            ans[i] = abs(rightSum - leftSum)

            leftSum += nums[i]

        return ans