
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited



def dfs2(graph, start, visited=None):
    if visited is None:
        visited = list()
    if start in visited:
        return visited

    visited.append(start)
    children = sorted(graph[start].difference(set(visited)))
    for next in children:
        dfs2(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def dfs2_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs2_paths(graph, next, goal, path + [next])




def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

if __name__ == "__main__":
    graph = {
        'A': set(['B', 'C']),
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),
        'D': set(['B']),
        'E': set(['B', 'F']),
        'F': set(['C', 'E'])
    }
    #      A
    #   B    C
    # D   E    F
    #
    #print(dfs(graph, 'A'))
    #print(dfs2(graph, 'A', None))
    #print(list(dfs_paths(graph, 'A', 'F')))
    #print(list(dfs2_paths(graph, 'A', 'F')))
    #print(bfs(graph, 'A'))
    print(shortest_path(graph, 'A', 'F'))# ['A', 'C', 'F'])

