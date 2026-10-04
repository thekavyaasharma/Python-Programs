# 678. Valid Parenthesis String - Medium
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0

        for c in s:
            if c =='(':
                high+=1
                low+=1
            elif c ==')':
                high -=1
                low -=1
            else:
                low-=1
                high+=1
            if high < 0 :
                return False
            elif low < 0:
                low = 0
        return low==0
        