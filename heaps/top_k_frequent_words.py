import heapq
from collections import Counter


class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word

    def __repr__(self):
        return str((self.freq, self.word))


# Time: O(n log k); Space: O(n + k)
def top_k_frequent(words, k):
    counter = Counter(words)
    heap = []

    for w, c in counter.items():
        heapq.heappush(heap, (Word(c, w)))

        if len(heap) > k:
            heapq.heappop(heap)

    heap.sort(key=lambda x: (-x.freq, x.word))
    return [x.word for x in heap]


# Test cases:
print(top_k_frequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(top_k_frequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
print(top_k_frequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=1))
print(top_k_frequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=3))
