# 2958. Length of Longest Subarray With at Most K Frequency - Medium
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = 0
        freq = defaultdict(int)

        for r, x in enumerate(nums):
            freq[x] +=1
            while freq[x] > k:
                freq[nums[left]]-=1
                left+=1
            cnt = max(cnt, r-left+1)
        return cnt

        