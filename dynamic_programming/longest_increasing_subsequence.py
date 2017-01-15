from math import ceil


def lis(x):
    """
    Longest Increasing Subsequence in a list
    :param x: list to analyze
    :return: list representing LIS
    """
    l = len(x)  # size of list

    # store index k of smallest value x[k] of lis of length j that ends at x[k]
    curr = [None] * (l + 1)
    # p[k] stores index of predecessor of x[k] in lis that ends at x[k]
    pred = [None] * l
    # best lis length so far
    longest = 0

    for i in range(0, l):
        # binary search for j <= longest, to get x[curr[j]] < x[i]
        lower = 1
        upper = longest

        while lower <= upper:
            mid = ceil((lower + upper) / 2)

            if x[curr[mid]] < x[i]:
                lower = mid + 1
            else:
                upper = mid - 1

        # lower = len of lis of x[i] + 1
        tent_longest = lower

        # pred of x[i] = last index of lis of len tent_longest - 1
        curr[tent_longest] = i
        pred[i] = curr[tent_longest - 1]

        # check if current subsequence is longer thant best
        if tent_longest > longest:
            longest = tent_longest

    # recover lis
    sequence = [None] * longest
    k = curr[longest]

    for i in range(longest - 1, -1, -1):
        sequence[i] = x[k]
        k = pred[k]

    return sequence
