class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self, word):
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.is_end

        return dfs(0, self.root)
