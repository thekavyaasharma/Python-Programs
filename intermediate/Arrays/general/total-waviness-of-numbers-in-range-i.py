# 3751 Medium
class Solution:
    def waviness(self,x:int)->int:
        s = str(x)
        count = 0
        for i in range(1,len(s)-1):
            if ((s[i] < s[i-1] and s[i] < s[i+1]) or 
                (s[i] > s[i-1] and s[i] > s[i+1])) :
                count +=1
        return count

    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness_count = 0

        for i in range(num1, num2+1):
            waviness_count += self.waviness(i)
        
        return waviness_count
        
                
