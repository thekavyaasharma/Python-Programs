# 227. Basic Calculator II - Medium
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = 0
        op = '+'
        s += '+'

        for ch in s:
            if ch == " ":
                continue
            if ch.isdigit():
                n = n * 10 + int(ch)
                continue

            if op == '+':
                stack.append(n)
            elif op == '-':
                stack.append(-n)
            elif op == '*':
                stack.append(stack.pop() * n)
            elif op =="/":
                stack.append(int(stack.pop()/n))
            op = ch
            n = 0
        return sum(stack)        