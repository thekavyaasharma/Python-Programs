# 3622. Check Divisibility by Digit Sum and Product - Easy
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s =0
        p =1
        temp = n
        while temp > 0:
            dig = temp % 10 
            s += dig
            p *= dig
            temp//=10
        return True if n % (s+p) == 0 else False