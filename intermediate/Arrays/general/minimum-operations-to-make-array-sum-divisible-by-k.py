# 3512. Minimum Operations to Make Array Sum Divisible by K - Easy
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k 


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in nums:
            count += i 
        return count % k

