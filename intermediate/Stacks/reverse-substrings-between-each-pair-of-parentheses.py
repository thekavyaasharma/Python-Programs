# 1190. Reverse Substrings Between Each Pair of Parentheses- Medium
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        link = [0] * n
        res , st = [],[]

        for i in range(n):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                j = st.pop()
                link[i] = j
                link[j] = i
        
        dr, i = 1, 0
        while i < n:
            if s[i] >= 'a':
                res.append(s[i])
            else:
                i = link[i]
                dr = -dr
            i += dr
        
        return ''.join(res)



        