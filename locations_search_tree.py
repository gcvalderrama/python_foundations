import math


class Node:
    def __init__(self):
        self.parent = None
        self.point = [0, 0]
        self.children = []


def distance(x, y):
    return math.sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))


def generate_three(root, locations, levels):
    if levels == 0:
        return
    for item in locations:
        temp = list(locations)
        temp.remove(item)
        n = Node()
        n.point = item
        n.parent = root
        root.children.append(n)
        generate_three(n, temp, levels-1)


def calculate_cost(node):
    cost = 0
    while node and node.parent:
        cost = cost + distance(node.point, node.parent.point)
        node = node.parent
    return cost


def generate_path(node):
    result = []
    while node and node.parent:
        result.append(node.point)
        node = node.parent
    result.reverse()
    return result



def search(root, state):
    if not root.children:
        if not state["path"]:
            state["cost"] = calculate_cost(root)
            state["path"] = root
        else:
            best_cost = state["cost"]
            current_cost = calculate_cost(root)
            if current_cost < best_cost:
                state["cost"] = current_cost
                state["path"] = root

    else:
        for item in root.children:
            search(item, state)

if __name__ == "__main__":
    locations = [[1, 2], [2, 4], [3, 5], [-5, 6], [5, -6],
                 [1, 3], [5, 7]]
    levels = 3
    root = Node()
    generate_three(root, locations, 3)
    state = {
        "cost": None,
        "path": None
    }
    search(root, state)
    print(generate_path(state["path"]))

    locations = [[1, 2], [3, 4], [1, -1]]
    root = Node()
    generate_three(root, locations, 2)
    state = {
        "cost": None,
        "path": None
    }
    search(root, state)
    print(generate_path(state["path"]))
