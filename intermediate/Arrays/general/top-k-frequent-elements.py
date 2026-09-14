# 347. Top K Frequent Elements - Medium
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        x = c.most_common(k)
        res = []
        for i in x:
            res.append(i[0])
        return res