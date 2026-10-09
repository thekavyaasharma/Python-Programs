# 1021. Remove Outermost Parentheses - Easy
class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        level = 0
        res = ""
        for i in s:
            if i == '(':
                if level>0:
                    res+=i
                level+=1
            else:
                level -=1
                if level > 0:
                    res += i
        return res
        