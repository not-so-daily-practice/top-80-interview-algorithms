def search_rotated_array_rec(arr, elem, left, right):
    """

    :param arr:
    :param elem:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        # element not present in arr
        return -1

    mid = int((left + right) / 2)  # middle

    if arr[mid] == elem:
        return mid

    # check if left - mid range is in order
    if arr[left] <= arr[mid]:
        if arr[left] <= elem <= arr[mid]:
            # element must lie in first half
            return search_rotated_array_rec(arr, elem, left, mid - 1)
        else:
            # element must lie in second half
            return search_rotated_array_rec(arr, elem, mid + 1, right)

    else:
        # left - mid range is not in order (contains pivot point)
        # therefore, mid - right range is in order
        if arr[mid] <= elem <= arr[right]:
            return search_rotated_array_rec(arr, elem, mid + 1, right)
        else:
            return search_rotated_array_rec(arr, elem, left, mid - 1)


def search_rotated_array(arr, elem):
    """

    :param arr:
    :param elem:
    :return:
    """
    return search_rotated_array_rec(arr, elem, 0, len(arr) - 1)
