def search_rotated_array_rec(arr, elem, left, right):
    """
    Given a sorted array that has been rotated around a point, find an element
    :param arr: rotated array (ex: 4, 5, 6, 7, 1, 2, 3
    :param elem: element to find
    :param left: left bound of search
    :param right: right bound of search
    :return: index of element (-1 if not found)
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
    Given a sorted array that has been rotated around a point, find an element
    :param arr: rotated array (ex: 4, 5, 6, 7, 1, 2, 3
    :param elem: element to find
    :return: index of element (-1 if not found)
    """
    return search_rotated_array_rec(arr, elem, 0, len(arr) - 1)
