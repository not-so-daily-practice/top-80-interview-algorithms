def bft(graph, s):
    """
    Breadth-First-Traversal
    :param graph: graph to traverse
    :param s: starting vertex
    :return:
    """
    visited = set()  # visited vertices
    queue = []  # vertices to visit

    queue.append(s)  # add starting vertex
    visited.add(s)

    while queue:  # while there remain unexplored vertices
        c = queue.pop(0)
        print(c)

        for i in graph.dic[c]:  # for each child of vertex
            if i not in visited:  # check if child has already been visited
                queue.append(i)  # if not, enqueue
                visited.add(i)
