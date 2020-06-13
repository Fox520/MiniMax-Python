class Node:
    value = None
    children = []

    def __init__(self, value, children):
        self.value = value
        self.children = children


def get_max(a1, a2):
    if a1 is None:
        return a2
    if a2 is None:
        return a1
    return max(a1, a2)


def get_min(a1, a2):
    if a1 is None:
        return a2
    if a2 is None:
        return a1
    return min(a1, a2)


def minimax(node: Node, isMaximize: bool):
    # Check if is leaf
    if node.children == []:
        return node.value
    if isMaximize:
        max_val = -100000
        for child in node.children:
            # Should perform minimization
            val = minimax(child, False)
            # Update maximum
            max_val = get_max(max_val, val)
        return max_val
    else:
        min_val = 10000
        for child in node.children:
            val = minimax(child, True)
            min_val = get_min(min_val, val)
        return min_val


leaf1 = Node(3, [])
leaf2 = Node(5, [])
leaf3 = Node(10, [])
minNode1 = Node(None, [leaf1, leaf2, leaf3])

leaf11 = Node(2, [])
leaf21 = Node(8, [])
leaf31 = Node(19, [])
minNode2 = Node(None, [leaf11, leaf21, leaf31])

leaf12 = Node(2, [])
leaf22 = Node(7, [])
leaf32 = Node(3, [])
minNode3 = Node(None, [leaf12, leaf22, leaf32])

rootNode = Node(None, [minNode1, minNode2, minNode3])

print(minimax(rootNode, True))
