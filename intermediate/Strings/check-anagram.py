'''
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

'''

# using hashmap 

def anagram(s,t):
    if len(s) != len(t):
        return False
    
    hmap = {}
    x = set(s)
    for i in x:
        hmap[i] = s.count(i)

    for i in t:
        if i not in s :
            return False
            break
        elif hmap[i] != t.count(i):
            return False
            break
    else:
        return True

s = "anagram"
t = "nagaram"

print(anagram(s,t))


s = "rat"
t = "car"

print(anagram(s,t))


s = ""
t = "hi"
print(anagram(s,t))

s = "race"
t = "care"
print(anagram(s,t))

s = "ab"
t = "a"
print(anagram(s,t))



# using pythonic way 
def anagram(s,t):
    if len(s) != len(t):
        return False
    
    x = set(s)
    for i in s:
        if i not in t or s.count(i) != t.count(i):
            return False
            break
    else:
        return True
    
print()
s = "anagram"
t = "nagaram"

print(anagram(s,t))


s = "rat"
t = "car"

print(anagram(s,t))


s = ""
t = "hi"
print(anagram(s,t))

s = "race"
t = "care"
print(anagram(s,t))

s = "ab"
t = "a"
print(anagram(s,t))



