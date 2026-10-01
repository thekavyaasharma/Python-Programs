#20. Valid Parentheses - Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stk = [-1]
        n = len(s)
        if n<=1 or n%2==1:
            return False
        for i in range(n):
            if s[i] in['(',"{",'[']:
                stk.append(s[i])
            elif s[i] ==')' and stk[-1] =='(':
                stk.pop()
            elif s[i]=='}' and stk[-1]=='{':
                stk.pop()
            elif s[i]==']' and stk[-1]=='[':
                stk.pop()
            else:
                return False
        return True if len(stk)==1 else False
        