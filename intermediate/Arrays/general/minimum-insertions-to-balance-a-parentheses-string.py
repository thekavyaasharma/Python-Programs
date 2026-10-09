
# 1541. Minimum Insertions to Balance a Parentheses String - Medium
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        o = 0
        ans = 0
        i = 0
        while( i < n):
            if s[i]=='(':
                o+=1
            else:
                if i < n-1 and s[i+1]==')':
                    i+=1
                else:
                    ans+=1
                if o==0:
                    ans+=1
                else:
                    o-=1
            i+=1
        return ans + ( 2*o)
        