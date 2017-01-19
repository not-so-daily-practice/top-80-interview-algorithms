def nth_magic_number(n):
    """
    Find the nth magic number
    A magic number can be expressed as a power of 5 or sum of unique powers of 5
    :param n: nth number to find
    :return: nth magic number
    """
    # note that magic numbers are represented as:
    # x * 5^1 + y * 5^2 + z * 5^3 + ...
    # given a number xyz...
    # for example: xyz => 010 => 0 * 5^1 + 1 * 5^1 + 0 * 5^2
    # so in essence, we are adding powers of 5 for each 1 in n
    res = 0
    powr = 1

    while n:
        # iterate over all bits
        powr *= 5

        if n & 1:
            # last bit of n is set
            res += powr

        # move to next bit
        n >>= 1  # shift

    return res
