def all_palindromic_partitions(word):
    """
    Given a string, print all possible palindromic partitions
    :param word: word to partition
    :return: set of all palindromic partitions
    """
    # sanity checks
    if word is None:
        return None

    res = set()  # set of all palindromes
    word_len = len(word)  # avoid recalculating on each call to check_radius_palindrome

    for i, c in enumerate(word):
        # start with a character and check if surrounding chars are equal on both sides (with a given radius)

        # check for longest odd-length palindrome
        res |= check_radius_palindrome(word, word_len, i, i)
        # check for longest ven-length palindrome
        res |= check_radius_palindrome(word, word_len, i, i + 1)

    return res


def check_radius_palindrome(word, word_len, i, j):
    """
    Given a string, and start/end positions, check if chars on each side of "center" match (is a palindrome)
    :param word: word to partition
    :param word_len: length of word (passed to avoid recomputing on each call
    :param i: start of range
    :param j: end of range
    :return: set of all palindromic partitions in range (of either even or odd-length depending on range provided)
    """
    res = set()
    while i >= 0 and j < word_len and word[i] == word[j]:
        # chars are equal, add to set
        res.add(word[i:j + 1])
        # expand range to check longer substring
        i -= 1
        j += 1

    return res
