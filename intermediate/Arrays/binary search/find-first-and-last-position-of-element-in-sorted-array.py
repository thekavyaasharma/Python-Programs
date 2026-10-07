# 34. Find First and Last Position of Element in Sorted Array- Medium
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1,-1]
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low+(high-low)//2

            if(nums[mid]==target):
                res[0]=mid
                high = mid -1
            
            elif nums[mid] > target:
                high = mid -1
            else:
                low = mid+1
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low+(high-low)//2

            if nums[mid]==target:
                res[1]=mid
                low = mid +1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return res
        