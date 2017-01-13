from graphs.breadth_first_traversal import bft
from graphs.depth_first_traversal import dft
from graphs.graph import Graph

default_graph = Graph()

default_graph.add_undirected_edge(1, 2)
default_graph.add_undirected_edge(1, 3)
default_graph.add_undirected_edge(1, 4)
default_graph.add_undirected_edge(2, 5)
default_graph.add_undirected_edge(2, 6)
default_graph.add_undirected_edge(4, 7)
default_graph.add_undirected_edge(4, 8)
default_graph.add_undirected_edge(5, 9)
default_graph.add_undirected_edge(5, 10)
default_graph.add_undirected_edge(7, 11)
default_graph.add_undirected_edge(7, 12)

default_graph_head = 1

print(bft(default_graph, default_graph_head))
print(dft(default_graph, default_graph_head))
