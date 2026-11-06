# 682. Baseball Game - Easy
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        x = []
        for i in operations:
            if i == 'C' and len(x) > 0:
                x.pop()
            elif i == '+' and len(x)>1:
                x.append(x[-1]+x[-2])
            elif i =='D' and len(x)>0:
                x.append(2*x[-1])
            else:
                x.append(int(i))
        return sum(x)
                


        