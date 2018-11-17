from collections import defaultdict
#Word Ladder II

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    res = []
    layer = {}
    layer[beginWord] = [[beginWord]]

    while layer:
        newlayer = defaultdict(list)
        for w in layer:
            if w == endWord:
                res.extend(k for k in layer[w])
            else:
                for i in range(len(w)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        neww = w[:i] + c + w[i + 1:]
                        if neww in wordList:
                            newlayer[neww] += [j + [neww] for j in layer[w]]

        wordList -= set(newlayer.keys())
        layer = newlayer

    return res

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None


def find_path(graph, start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None:
        path = []
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    if start_vertex not in graph:
        return None
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = find_path(graph, vertex, end_vertex, path)
            if extended_path:
                return extended_path
    return None

def find_all_paths(graph, start_vertex, end_vertex, path=[]):
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return [path]
    if start_vertex not in graph:
        return []
    paths = []
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_paths = find_all_paths(graph, vertex, end_vertex, path)
            for p in extended_paths:
                paths.append(p)
    return paths

def dijkstra(graph, source, dest):

    # 1. Mark all nodes unvisited and store them.
    # 2. Set the distance to zero for our initial node
    # and to infinity for other nodes.

    vertices = graph.keys()
    distances = {}
    inf = float("inf")

    distances = {vertex: inf for vertex in vertices}
    previous_vertices = {
        vertex: None for vertex in vertices
    }
    distances[source] = 0

    while vertices:
        # 3. Select the unvisited node with the smallest distance,
        # it's current node now.
        current_vertex = min(vertices, key=lambda vertex: 1)

        # 6. Stop, if the smallest distance
        # among the unvisited nodes is infinity.
        if distances[current_vertex] == inf:
            break

        # 4. Find unvisited neighbors for the current node
        # and calculate their distances through the current node.
        for neighbour, cost in graph[current_vertex]:
            alternative_route = distances[current_vertex] + cost

            # Compare the newly calculated distance to the assigned
            # and save the smaller one.
            if alternative_route < distances[neighbour]:
                distances[neighbour] = alternative_route
                previous_vertices[neighbour] = current_vertex

        # 5. Mark the current node as visited
        # and remove it from the unvisited set.
        vertices.remove(current_vertex)

    path, current_vertex = deque(), dest
    while previous_vertices[current_vertex] is not None:
        path.appendleft(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    if path:
        path.appendleft(current_vertex)
    return path

if __name__ == "__main__":
    beginWord = "hot"
    endWord = "dog"
    #wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    wordList = ["hot", "dog"]
    wordList = set([beginWord] + wordList)
    graph = dict()
    for item in wordList:
        graph[item] = []
        for other in wordList:
            distance = 0
            for i in range(len(item)):
                if item[i] != other[i]:
                    distance += 1
            if distance == 1:
                graph[item].append(other)

    paths = find_all_paths(graph, beginWord, endWord)
    min_len = min(paths)
    print(min_len)
    for p in paths:
        if len(p) == len(min_len):
            print(p)



    #Output:
    #[
        #["hit","hot","dot","dog","cog"],
        #["hit","hot","lot","log","cog"]
    #]
    findLadders(beginWord, endWord, wordList)


