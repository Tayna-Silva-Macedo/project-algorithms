def reverse(word):
    if len(word) == 1:
        return word
    else:
        return reverse(word[1:]) + word[0]


def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False

    word_reversed = reverse(word)
    return word_reversed.lower() == word.lower()
