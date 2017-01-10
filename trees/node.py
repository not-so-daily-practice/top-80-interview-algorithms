class Node(object):
    """
    Binary Node
    """

    def __init__(self, data):
        """
        Initialize node
        :param data: data to store
        """
        self.data = data
        self.left = None  # left child
        self.right = None  # right child
