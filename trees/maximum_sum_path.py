curr = float("-inf")


def max_sum_path(root):
    """
    Find path in tree that has largest sum possible
    :param root: root node of tree
    :return: max sum
    """
    # base case
    if root is None:
        return 0

    # recurse on left and right
    left_sum, right_sum = max_sum_path(root.left), max_sum_path(root.right)

    # sum of path passing through a single child
    # compare passing through left vs right child, or not traversing children
    max_sum_node = max(max(left_sum, right_sum) + root.data, root.data)

    # sum of path passing through both children
    # compare passing through both left and right children, or staying with max_sum_node
    max_sum_pass = max(left_sum + right_sum + root.data, max_sum_node)

    # check if path is better than worst-
    global curr
    curr = max(curr, max_sum_pass)

    return max_sum_node


def max_sum_path_tree(root):
    """
    Find path in tree that has largest sum possible
    :param root: root node of tree
    :return: max sum
    """
    max_sum_path(root)

    return curr
