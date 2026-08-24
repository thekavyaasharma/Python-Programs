# 229. Majority Element II - Medium
# Boyer-Moore Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #freq = Counter(nums)
        freq = defaultdict(int)

        for i in nums:
            freq[i] +=1

        t = len(nums)//3
        res = []

        for i in freq:
            if freq[i] > t:
                res.append(i)
        return res
        