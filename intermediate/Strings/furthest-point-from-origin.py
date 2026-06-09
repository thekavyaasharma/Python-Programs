# 2833. Furthest Point From Origin. EASY

class Solution:

    def origin(self,s):

        right = s.replace('_', 'R')
        x = (right.count('R') - right.count('L'))

        left = s.replace('_', 'L')
        y = abs(left.count('R') - left.count('L'))
        return max(x,y)
    
s = Solution()
l = "_R__LL_"
print(s.origin(l))

l =  "L_RL__R"
print(s.origin(l))

l =  "_______"
print(s.origin(l))
