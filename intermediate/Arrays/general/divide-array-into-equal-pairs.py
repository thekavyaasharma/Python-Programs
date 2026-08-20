# 2206. Divide Array Into Equal Pairs - Easy
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set(nums)
        count = 0
        for i in s:
            count +=nums.count(i)//2
        return True if count == len(nums)//2 else False

        ss