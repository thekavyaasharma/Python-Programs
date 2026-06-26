# 3737. Count Subarrays With Majority Element I - Medium
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSubarray = 0

        for left in range(n):
            majorityElementCount = 0
            for right in range(left , n):

                if nums[right] == target :
                    majorityElementCount += 1
                length = right - left + 1

                if majorityElementCount > length // 2:
                    totalSubarray += 1
            
        return totalSubarray
