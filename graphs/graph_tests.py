from graphs.breadth_first_traversal import bft
from graphs.depth_first_traversal import dft
from graphs.graph import Graph
from graphs.shortest_path_source_all_vertices import shortest_path_all_vertices, get_path

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

graph = {
    'a': {'a': 2, 'b': 2},
    'b': {'c': 1, 'd': 4},
    'c': {'a': 1, 'd': 1},
    'd': {'c': 1, 'e': 1},
    'e': {}
}

print(shortest_path_all_vertices(graph, 'a')[0])
print(get_path(graph, 'a', 'd'))
