'''
3633. Earliest Finish Time for Land and Water Rides I

Easy

'''


class Solution:
    def calFinishTime(self, ls, ld, ws, wd):
        result = float('inf')
        for i in range(len(ls)):
            result += min(result, ls[i]+ld[i])

        ans = float('inf')
        for j in range(len(ws)):
            ans = min(ans, max(result, ws[i])+wd[i])
        
        return ans

    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], 
    waterStartTime: List[int], waterDuration: List[int]) -> int:
        return min(self.calFinishTime(landStartTime, landDuration, waterStartTime, waterDuration), 
        self.calFinishTime(waterStartTime, waterDuration, landStartTime, landDuration))

