# Given an undirected graph, determine if a cycle exists in the graph.
import unittest


def is_cycle(graph, key, state, parent):
    state[key] = True
    if key not in graph:
        return False
    for i in graph[key]:
        if i not in state:
            if is_cycle(graph, i, state, key):
                return True
        elif parent != i:
            return True
    return False


def find_cycle(graph):
    state = dict()
    for key in graph.keys():
        if key not in state:
            if is_cycle(graph, key, state, -1):
                return True
    return False


class Test(unittest.TestCase):
    def test_case(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        result = find_cycle(graph)
        self.assertFalse(result)

    def test_case_true(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        graph['c'] = graph
        result = find_cycle(graph)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
