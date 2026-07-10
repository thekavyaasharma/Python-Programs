# 38 - Count and Say - Medium 

class Solution :
    def count(self,seq):
        count = 0
        curr = seq[0]
        ans = ""

        for num in seq:
            if num == curr:
                count +=1
            else:
                ans += f'{count}{curr}'
                curr = num
                count = 1
        return ans + f"{count}{curr}"
    
    def countAndSay(self, n):
        if n == 1:
            return "1"
        return self.count(self.countAndSay(n-1))