# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum - Medium
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        res = n+1
        dp = [n] * (n+1)
        total = 0
        i = 0

        for j in range(n):
            total += arr[j]

            while total > target:
                total -= arr[i]
                i+=1
            
            dp[j+1] = dp[j]

            if(total==target):
                length = j-i+1
                res = min(res,length+dp[i])

                dp[j+1] = min(dp[j], length)

        return res if res!= n+1 else -1        