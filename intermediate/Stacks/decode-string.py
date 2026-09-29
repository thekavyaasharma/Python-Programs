# 394. Decode String - Medium
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        curNum = 0
        curStr = ''

        for c in s:
            if c == '[':
                st.append(curStr)
                st.append(curNum)
                curStr = ""
                curNum = 0
            elif c == ']':
                num = st.pop()
                prevStr = st.pop()
                curStr = prevStr + num * curStr
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                curStr += c
        return curStr

        