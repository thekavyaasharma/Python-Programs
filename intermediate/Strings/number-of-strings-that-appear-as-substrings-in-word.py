# 1967. Number of Strings That Appear as Substrings in Word - Easy
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns :
            if pattern in word:
                count +=1
        return count 