#1111. Maximum Nesting Depth of Two Valid Parentheses Strings - Medium
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = [None] * len(seq)
        depth = 0
        for i, c in enumerate(seq) :
            if c=='(':
                depth +=1
                ans[i]=depth%2

            else:
                ans[i] = depth%2
                depth-=1
        return ans