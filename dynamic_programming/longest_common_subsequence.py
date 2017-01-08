from itertools import product


def lcs(str1, str2):
    """
    Find the longest common subsequence of two strings
    :param str1: first string to check
    :param str2: second string to check
    :return: longest common subsequence
    """
    m, n = len(str1), len(str2)

    # 2d array to store subproblems
    # padded on top and left with empty strings
    sub = [[""] * (n + 1) for i in range(m + 1)]

    for i, j in product(range(m + 1), range(n + 1)):
        if i == 0 or j == 0:
            # comparing empty strings, maintain padding
            continue

        if str1[i - 1] == str2[j - 1]:
            # same character, add to previous largest solution
            sub[i][j] = sub[i - 1][j - 1] + str1[i - 1]
        else:
            # characters don't match
            # current solution must be the largest previous solution
            sub[i][j] = sub[i - 1][j] if len(sub[i - 1][j]) > len(sub[i][j - 1]) else sub[i][j - 1]

    return sub[m][n]


str1 = "abcfdcbab"
str2 = "acbgdcb"

print(lcs(str1, str2))
