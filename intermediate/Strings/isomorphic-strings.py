# 205 - ISOMORPHIC STRINGS - EASY
class Solution :
    def isIsomorphic(self, s,t):
        hashmap_s = {}
        hashmap_t = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = i
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = i
            if hashmap_s[s[i]] != hashmap_t[t[i]]:
                return False
        
        return True 

