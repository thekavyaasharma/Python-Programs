# 1614. Maximum Nesting Depth of the Parentheses - Easy
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        depth = 0
        for i in s:
            if i == ')':
                depth -=1
                continue
            elif i != '(':
                continue
            depth +=1

            if depth > res:
                res = depth
        return res
        