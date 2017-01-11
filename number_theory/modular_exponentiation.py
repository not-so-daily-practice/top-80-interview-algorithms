def mod_exp(x, y, p):
    """
    Modular exponentiation (power in modular arithmetic)
    Yields (x^y) % p
    :param x: base
    :param y: exponent
    :param p: mod
    :return: result of (x^y) % p
    """
    result = 1  # init result

    x = x % p  # mod to prevent overflow with large x

    while (y > 0):
        if not y % 2 == 0:  # check if odd
            result = (result * x) % p

        # at this point, must be even
        y = int(y / 2)
        x = (x * x) % p  # restore

    return result
