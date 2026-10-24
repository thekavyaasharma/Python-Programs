# 2409. Count Days Spent Together - Easy
class Solution(object):
    def countDaysTogether(self, a,b,c,d):
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        def today(s):
            m = int(s[:2])
            d = int(s[3:])
            res = d
            for i in range(m-1):
                res+=days[i]
            return res
        a,b = today(a), today(b)
        c,d = today(c), today(d)

        st = max(a,c)
        end = min(b,d)
        return end-st+1 if st<=end else 0