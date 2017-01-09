def recursive_binary_search(arr, element):
    """
    Given a sorted list of elements, search for item
    :param arr: sorted list
    :param element: element to find
    :return: index of element (-1 if not found)
    """
    return recursive_bounded_binary_search(arr, element, 0, len(arr))


def recursive_bounded_binary_search(arr, element, left, right):
    """
    Given a sorted list of elements, search for item between the left and right indices
    :param arr: sorted list
    :param element: element to find
    :param left: left bound of list
    :param right: right bound of list
    :return: index of element (-1 if not found)
    """
    if right < left:
        return -1

    middle = left + round((right - left) / 2)
    if arr[middle] == element:
        return middle

    if arr[middle] < element:
        return recursive_bounded_binary_search(arr, element, middle + 1, right)
    else:
        return recursive_bounded_binary_search(arr, element, left, middle - 1)


def iterative_binary_search(arr, element):
    """
    Given a sorted list of elements, search for an item
    :param arr: sorted list
    :param element: element to find
    :return: index of element (-1 if not found)
    """
    left, right = 0, len(arr)
    while left < right:
        middle = left + round((right - left) / 2)

        if arr[middle] == element:
            return middle

        if arr[middle] < element:
            left = middle + 1
        else:
            right = middle - 1

    return -1
