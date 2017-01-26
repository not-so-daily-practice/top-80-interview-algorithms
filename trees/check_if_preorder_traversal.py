def check_if_preorder_traversal(arr):
    """
    Check if array is a preorder traversal of a binary tree
    :param arr: array to check
    :return: boolean True if valid, False otherwise
    """
    stack = []  # stack to hold nodes

    # root should have min value
    root = float("-inf")

    # iterate over arr
    for i in arr:
        if i < root:
            # node is less than root, violates binary tree rules
            return False

        # while i is in right subtree of the top of the stack
        while stack and stack[-1] < i:
            # remove nodes smaller than i
            # make last removed node the new root
            root = stack.pop()

        # now, stack must be empty, or i is less than root
        stack.append(i)  # push i

    return True
