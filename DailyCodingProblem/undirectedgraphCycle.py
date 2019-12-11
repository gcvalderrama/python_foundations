# Given an undirected graph, determine if a cycle exists in the graph.
import unittest


def find_cycle(graph):
    pass


class Test(unittest.TestCase):
    def test_case(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        find_cycle(graph)

    def test_case_true(self):
        graph = {
            'a': {'a2': {}, 'a3': {}},
            'b': {'b2': {}},
            'c': {}
        }
        graph['c'] = graph

if __name__ == "__main__":
  unittest.main()
