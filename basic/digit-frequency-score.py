# 3945. Digit Frequency Score - Easy
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        temp = str(n)
        res = 0
        for i in set(temp):
            res += int(i) * temp.count(i)
        return res
        