# Time: O(n^2); Space: O(n)
def sort_sentence(s):
    words = s.split()
    original_s = [' '] * len(words)

    for word in words:
        idx = int(word[-1])
        original_s[idx - 1] = word[:-1]  # O(n) slicing ?

    return ' '.join(original_s)


# Test case:
print(sort_sentence('is2 sentence4 This1 a3'))
print(sort_sentence('Myself2 Me1 I4 and3'))
