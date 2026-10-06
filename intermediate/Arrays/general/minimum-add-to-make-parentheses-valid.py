# 921. Minimum Add to Make Parentheses Valid - Medium
class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        ob = mn = 0
        for c in s:
            if c=='(':
                ob+=1
            else:
                if ob>=1:
                    ob-=1
                else:
                    mn+=1
        return mn+ob
        