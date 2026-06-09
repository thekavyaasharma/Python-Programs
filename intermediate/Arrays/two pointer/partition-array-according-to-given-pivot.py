#2161 MEDIUM 
class Solution :
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        n = len(nums)
        result = [0] * n

        i, j = 0, n - 1
        left , right = 0, n -1 

        while i < n:
            if nums[i] < pivot:
                result[left] = nums[i]
                left +=1
            if nums[j] > pivot:
                result[right] = nums[j]
                right -= 1
            i += 1
            j -= 1
        
        # insert pivot values at middle 
        while left <= right:
            result[left] = pivot
            left += 1
        
        return result

