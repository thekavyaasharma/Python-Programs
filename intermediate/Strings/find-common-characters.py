#1002. Find Common Characters - Easy
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) < 2:
            return [ w for w in words[0]]
        res = []
        word1 = set(words[0])
        for ch in word1:
            freq = min([word.count(ch) for word in words])
            res += [ch] * freq
        return res
        