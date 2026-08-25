# 3718. Smallest Missing Multiple of K - Easy
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        curr = k
        while curr in nums:
            curr +=k
        return curr