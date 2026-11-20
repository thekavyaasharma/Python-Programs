# 3041. Maximize Consecutive Elements in an Array After Modification - Hard
class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        dp = {}
        nums.sort()
        for num in nums:
            dp[num+1] = dp.get(num,0) +1
            dp[num] = dp.get(num-1,0) +1
            ans = max(ans,dp[num],dp[num+1])
        return ans
        