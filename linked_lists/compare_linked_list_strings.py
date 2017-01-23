def compare_linked_list_strings(ll_str_1, ll_str_2):
    """
    Compare two strings represented as linked lists
    :param ll_str_1: linked list 1
    :param ll_str_2: linked list 2
    :return: -1 if list 1 is lexicographically greater than list 2, 0 if equal, -1 if less than
    """
    while ll_str_1 and ll_str_2 and ll_str_1.data == ll_str_2.data:
        # both lists are not finished
        # current char is equal
        ll_str_1 = ll_str_1.next  # move to next char
        ll_str_2 = ll_str_2.next  # move to next char

    if ll_str_1 and ll_str_2:
        # lists still contain chars, so chars must be different
        if ll_str_1.data > ll_str_2.data:
            # list 1 is greater
            return 1
        else:
            # list 2 is greater
            return -1

    # lists must be if different lengths
    if ll_str_1 and not ll_str_2:
        # list 1 is longer than list 2
        return 1

    if not ll_str_1 and ll_str_2:
        # list 2 is longer than list 1
        return -1

    # lists are identical
    return 0
