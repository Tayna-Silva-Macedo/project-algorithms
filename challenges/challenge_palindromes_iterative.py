def reverse(word):
    reversed_word = ""

    for index in range(len(word) - 1, -1, -1):
        reversed_word += word[index]

    return reversed_word


def is_palindrome_iterative(word):
    if not word:
        return False

    word_reversed = reverse(word)
    return word_reversed.lower() == word.lower()
