# 451. Sort Characters By Frequency - Medium
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        x = sorted(c.items(),key = lambda w : (w[1],w[0]), reverse = True)
        c = dict(x)
        res = ""
        for k,v in c.items():
            res+= k*v
        return res
            

        