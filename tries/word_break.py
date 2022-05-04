class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True


def word_break(s, word_dict):
    # Create a Trie and insert the word dict
    trie = Trie()

    for word in word_dict:
        trie.insert(word)

    # Check if we can split the string
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True

    for i in range(n - 1, -1, -1):
        node = trie.root

        for j in range(i + 1, n + 1):
            char = s[j - 1]
            if char not in node.children:
                break  # s[i:j] not exist in our trie
            node = node.children[char]

            if node.is_end_of_word and dp[j]:
                dp[i] = True
                break

    return dp[0]


# Test cases:
print(word_break(s="leetcode", word_dict=["leet", "code"]))
