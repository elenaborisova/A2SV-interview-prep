from collections import deque


def ladder_length(begin_word, end_word, word_list):
    word_list = set(word_list)
    queue = deque([(begin_word, 1)])

    while queue:
        word, count = queue.popleft()

        if word == end_word:
            return count

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word in word_list:
                    word_list.remove(next_word)
                    queue.append((next_word, count + 1))

    return 0


# Test cases:
print(ladder_length(begin_word="hit", end_word="cog", word_list=["hot", "dot", "dog", "lot", "log", "cog"]))
print(ladder_length(begin_word="hit", end_word="cog", word_list=["hot", "dot", "dog", "lot", "log"]))
print(ladder_length(begin_word="hot", end_word="dog", word_list=["hot", "dog", "dot"]))
print(ladder_length(begin_word="a", end_word="c", word_list=["a", "b", "c"]))
