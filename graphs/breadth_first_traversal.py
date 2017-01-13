def bft(graph, s):
    """
    Breadth-First-Traversal
    :param graph: graph to traverse
    :param s: starting vertex
    :return: set of BFS-visited vertices
    """
    visited = []  # visited vertices
    queue = []  # vertices to visit

    queue.append(s)  # add starting vertex

    while queue:  # while there remain unexplored vertices
        c = queue.pop(0)  # current vertex

        if c not in visited:
            visited.append(c)
            queue.extend(graph.dic[c] - set(visited))  # add unvisited children

    return visited
