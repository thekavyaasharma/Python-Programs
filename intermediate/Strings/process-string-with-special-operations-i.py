# 3612 - medium - Process String with Special Operations I
class Solution:
    def processStr(self, s: str) -> str:
        result = []

        for ch in s:
            if ch.islower():
                result.append(ch)
            elif ch == '#':
                result.extend(result)
            elif ch == '%':
                result.reverse()
            elif ch == '*' and len(result)!=0:
                result.pop()

        
        return "".join(result)