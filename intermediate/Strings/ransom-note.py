# 383 - Ransom Note - Easy
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = [0] * 26 

        if len(ransomNote) > len(magazine):
            return False
        
        for ch in magazine:
            frequency[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            if frequency[ord(ch) - ord('a')] == 0:
                return False
            frequency[ord(ch)- ord('a')] -=1
        return True 
