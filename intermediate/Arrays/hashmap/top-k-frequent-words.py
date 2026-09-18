#692. Top K Frequent Words - Medium
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = Counter(words)
        sorted_freq = sorted(freq.keys(), key = lambda w: (-freq[w],w))
        return sorted_freq[:k]
        