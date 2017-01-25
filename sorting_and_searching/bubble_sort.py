def bubble_sort(arr):
    """
    Bubble sort an array
    :param arr: list to sort
    :return: sorted list
    """
    n = len(arr)
    for i in range(n):
        # iterate over list
        swapped = False
        for j in range(n - i - 1):
            # iterate over remaining unsorted elements
            if arr[j] > arr[j + 1]:
                # if current element is greater than next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                swapped = True

        if not swapped:
            # didn't swap, so sorted
            break

    return arr
