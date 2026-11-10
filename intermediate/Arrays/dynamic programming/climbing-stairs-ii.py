# 3693. Climbing Stairs II - Medium
class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        costs = [0] + costs
        dp = [float('inf')] * (n+3)
        dp[n] = costs[n]
        for i in range(n-1,-1,-1):
            dp[i] = costs[i] + min(dp[i+1]+1, dp[i+2]+4, dp[i+3]+9)
        return dp[0]      