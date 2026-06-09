# 3689. Maximum Total Subarray Value I - MEDIUM

class Solution :
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        result = max(nums) - min(nums)
        return result * k
    
class Solution2 :
    def maxTotalValue2(self, nums: list[int], k: int) -> int:

        maximum = nums[0]
        minimum = nums[0]

        for i in range(len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
            elif nums[i] < minimum:
                minimum = nums[i]

        result = maximum - minimum
        return result * k 