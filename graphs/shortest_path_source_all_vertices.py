from copy import copy


def shortest_path_all_vertices(graph, start):
    """
    Dijkstra's algorithm
    :param graph: dict representation of graph
    :param start: starting vertex
    :return: list representing path from start to all vertices
    """
    distances = {}  # Dictionary of final distance for each node
    parent = {}  # Dictionary of parent of each node

    # Initially, the starting vertex distance is 0, and every other vertex is infinity
    # Each vertex' parent is "none"
    for v in graph:
        parent[v] = "none"
        if v == start:
            distances[v] = 0
        else:
            distances[v] = float("inf")

    nonFinal = copy(distances)

    # While there are nonFinal vertices
    while nonFinal:
        v = min(nonFinal, key=nonFinal.get)  # Let v be the vertex in nonFinal with the smallest distance
        nonFinal.pop(v)  # Remove v from nonFinal

        # For every neighbor u of v
        for u in graph[v]:
            if distances[u] > distances[v] + graph[v][u]:  # If u's distance > v's distance + weight of the edge (v, u)
                distances[u] = distances[v] + graph[v][u]  # Update u's distance to v's distance + weight (v, u)
                nonFinal[u] = distances[u]
                parent[u] = v  # Set it's parent to v

    return distances, parent


def get_path(graph, start, end):  # Print path from start to given vertex
    parent = shortest_path_all_vertices(graph, start)[1]

    current = end
    path = []
    while parent[current] != "none":
        path.append(current)
        current = parent[current]
    path.append(current)
    path.reverse()

    return path
