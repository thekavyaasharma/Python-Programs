'''
Medium - 3
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def longest_substring(s):
    res = 0
    temp = ""

    for ch in s:
        if ch not in temp:
            temp += ch
        else :
            temp = ""
        res = max(res, len(temp))
    
    return res

print(longest_substring('pwwkew'))

print(longest_substring('bbbb'))

print(longest_substring('abcabcabc'))

