def reverse_except_special(arr):
    """
    Given an array, reverse it without changing the positions of special characters
    :param arr: array to reverse
    :return: reversed array
    """
    arr = list(arr)
    left = 0
    right = len(arr) - 1

    while left < right:
        if not arr[left].isalpha():
            left += 1
        elif not arr[right].isalpha():
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    arr = "".join(arr)

    return arr
