# 442. Find All Duplicates in an Array - Medium
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for i in c:
            if c[i] == 2:
                res.append(i)
        return res
        