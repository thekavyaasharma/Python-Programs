# 856. Score of Parentheses - Medium
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s)==2:
            return 1
        depth = score = 0
        for x,i in enumerate(s):
            if i =='(':
                depth+=1
            else:
                depth -=1
                if s[x-1] =='(':
                    score += 1<<depth
        return score
        