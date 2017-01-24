def edit_distance(str_1, str_2):
    """
    Find the minimum number of edits required to convert str_1 to str_2
    Operations are: insert, remove, replace
    :param str_1: original string
    :param str_2: transformed string
    :return: int number of edits required to transform str_1 to str_2
    """
    return edit_distance_dp(str_1, len(str_1), str_2, len(str_2))


def edit_distance_dp(str_1, m, str_2, n):
    """
    Find the minimum number of edits required to convert str_1 to str_2
    Operations are: insert, remove, replace
    :param str_1: original string
    :param m: index in str_1
    :param str_2: transformed string
    :param n: index in str_2
    :return: int number of edits required to transform str_1 to str_2
    """
    # table for storing sub-problems
    sub = [[0 for i in range(n + 1)] for j in range(m + 1)]  # padded for empty cases

    # fill table
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                # str_1 is empty, or we have not selected any substring of it
                sub[i][j] = j  # the difference is all of str_2, equivalent to len(str_2) = j removals
            elif j == 0:
                # str_2 is empty, or we have not selected any substring of it
                sub[i][j] = i  # the difference is all of str_1, equivalent to len(str_1_ = i removals
            elif str_1[i - 1] == str_2[j - 1]:
                # last chars are equal, so no edits needed; continue for sub-problems
                sub[i][j] = sub[i - 1][j - 1]
            else:
                # last chars are not equal, solve for all 3 subproblems
                insert_char = sub[i][j - 1]
                remove_char = sub[i - 1][j]
                replace_char = sub[i - 1][j - 1]
                sub[i][j] = 1 + min(insert_char, remove_char, replace_char)

    return sub[m][n]  # solution lies in last cell
