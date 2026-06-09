# 2833. Furthest Point From Origin. EASY

class Solution:

    def origin(self,s):

        right = s.replace('_', 'R')
        x = (right.count('R') - right.count('L'))

        left = s.replace('_', 'L')
        y = abs(left.count('R') - left.count('L'))
        return max(x,y)

class Solution2:

    def origin(self,s):
        right = 0
        left = 0
        blank = 0

        for ch in s:
            if ch == 'R':
                right +=1
            elif ch == 'L':
                left +=1
            else:
                blank +=1
        
        return abs(right - left ) + blank
    
s = Solution2()
l = "_R__LL_"
print(s.origin(l))

l =  "L_RL__R"
print(s.origin(l))

l =  "_______"
print(s.origin(l))
