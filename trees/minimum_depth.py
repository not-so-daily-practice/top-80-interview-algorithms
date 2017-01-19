def min_depth(root):
    """
    Find minimum depth of binary tree
    Done by performing a breadth-first traversal
    :param root: root of tree
    :return: depth of tree
    """
    depth = 0
    if root is None:
        return depth

    queue = [{"node": root, "depth": 1}]  # nodes to visit

    while queue:
        qd = queue.pop(0)
        node = qd["node"]
        depth = qd["depth"]

        if node.left is None and node.right is None:
            return depth

        if node.left:
            queue.append({"node": node.left, "depth": depth + 1})

        if node.right:
            queue.append({"node": node.right, "depth": depth + 1})
