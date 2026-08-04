# 3731. Find Missing Elements - Easy
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        mn = min(nums)
        mx = max(nums)

        for i in range(mn , mx+1):
            if i not in nums:
                res.append(i)
        return res 
