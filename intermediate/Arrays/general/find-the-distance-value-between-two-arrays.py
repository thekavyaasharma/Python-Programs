# 1385. Find the Distance Value Between Two Arrays- Easy
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=0
        for i in arr1:
            for j in arr2:
                if abs(i-j) <= d:
                    break
            else:
                ans+=1
        return ans
        