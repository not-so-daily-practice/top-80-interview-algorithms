from collections import defaultdict


class Graph(object):
    """
    Dictionary representation of a graphs
    """

    def __init__(self):
        """
        Create dict where graphs is of format start_node : [end_node_1, ..., end_node_n]
        """
        self.dic = defaultdict(set)

    def add_edge(self, u, v):
        """
        Add directed edge
        :param u: starting vertex
        :param v: ending vertex
        :return: True if able to add
        """
        try:
            self.dic[u].add(v)
            return True
        except:
            return False

    def add_undirected_edge(self, u, v):
        """
        Add undirected edge
        :param u: starting vertex
        :param v: ending vertex
        :return: True if able to add
        """
        try:
            self.add_edge(u, v)
            self.add_edge(v, u)
            return True
        except:
            return False

    def remove_edge(self, u, v):
        """
        Remove directed edge
        :param u: starting vertex
        :param v: ending vertex
        :return: True if able to remove
        """
        try:
            self.dic[u].remove(v)
            return True
        except:
            return False

    def remove_undirected_edge(self, u, v):
        """
        Remove undirected edge
        :param u: starting vertex
        :param v: ending vertex
        :return: True if able to remove
        """
        try:
            self.remove_edge(u, v)
            self.remove_edge(v, u)
            return True
        except:
            return False
