# 1291 - Sequential Digits - MEDIUM 
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        l = str(low)
        h = str(high)
        res = []

        for length in range(len(l), len(h)+1):
            for start in range(0, 10-i):
                num = int(str[start:start+i])
                if low <= num <= high:
                    res.append(num)
        return res 