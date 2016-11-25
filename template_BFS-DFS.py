def bfs(graph, start, end):
    """
    detect if the start is connected to the end by BFS
    :param graph: a dictionary representing a graph
    :param start: the start vertex
    :param end: the end vertex
    :return: tuple
    """
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            if current not in graph:
                continue
            path.append(current)
            if current == end:
                return True, path
            visited = visited + graph[current]
    return False, path


def dfs(graph, start, end):
    """
    detect if the start is connected to the end by DFS
    :param graph: a dictionary representing a graph
    :param start: the start vertex
    :param end: the end vertex
    :return: tuple
    """
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            if current not in graph:
                continue
            path.append(current)
            if current == end:
                return True, path
            visited = graph[current] + visited
    return False, path


def bfs_portion(visited, next_vertices):
    return visited + next_vertices


def dfs_portion(visited, next_vertices):
    return next_vertices + visited


def template_search(graph, start, end, action):
    """
    detect if the start is connected to the end
    :param graph: a dictionary representing a graph
    :param start: the start vertex
    :param end: the end vertex
    :param action: the searching method
    :return: tuple
    """
    path = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in path:
            if current not in graph:
                continue
            path.append(current)
            if current == end:
                return True, path
            visited = action(visited, graph[current])
    return False, path


if __name__ == '__main__':
    graph = {
        'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
        'Mannheim': ['Karlsruhe'],
        'Karlsruhe': ['Augsburg'],
        'Augsburg': ['Munchen'],
        'Wurzburg': ['Erfurt', 'Nurnberg'],
        'Nurnberg': ['Munchen'],
        'Kassel': ['Munchen'],
        'Erfurt': [],
        'Stuttgart': ['Nurnberg'],
        'Munchen': []
    }

    while True:
        start = raw_input('choose your start city(type "exit" to exit)>')
        if start == 'exit':
            break
        end = raw_input("choose your end city>")

        bfs_path = bfs(graph, start, end)
        dfs_path = dfs(graph, start, end)
        t_bfs_path = template_search(graph, start, end, bfs_portion)
        t_dfs_path = template_search(graph, start, end, dfs_portion)

        print 'bfs {}-{}: {}'.format(start, end, bfs_path[1] if bfs_path[0] else 'disconnected')
        print 'dfs {}-{}: {}'.format(start, end, dfs_path[1] if dfs_path[0] else 'disconnected')
        print 't_bfs {}-{}: {}'.format(start, end, t_bfs_path[1] if t_bfs_path[0] else 'disconnected')
        print 't_dfs {}-{}: {}'.format(start, end, t_dfs_path[1] if t_dfs_path[0] else 'disconnected')
