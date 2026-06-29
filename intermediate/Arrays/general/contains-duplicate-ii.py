# 219 - Contains Duplicates II - EASY

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, v in enumerate(nums):
            if v in seen and i - seen[v] <= k:
                return True
            else:
                seen[v] = i
        return False