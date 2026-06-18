# 3614. Process String with Special Operations II - HARD

class Solution:
    def processStr(self, s : str , k : int) -> str:

        length = 0

        for ch in s :
            if ch == "*":
                length = max(0, length-1)
            elif ch == "#":
                length *= 2
            elif ch != "%":
                length +=1

        if k >= length :
            return "."
        
        for i in range(len(s)-1 ,-1 ,-1):
            ch = s[i]

            if ch == "*":
                length +=1
            elif ch == "#":
                half = length // 2
                if k >= half :
                    k -= half
                length = half 
            elif ch == "%":
                k = length-1-k
            
            else:
                if k == length-1:
                    return ch 
                length -= 1
        
        return "."
            