from collections import deque

class HelperNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)
        
def construct_binary_tree(values):
    nodes = {}
    root = HelperNode(values[0])
    q = deque()
    q.append(root)
    i = 0
    while q:
        to_proc = q.popleft()
        nodes[to_proc.data] = to_proc
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(values):
            left_child = HelperNode(values[left_index])
            to_proc.children.append(left_child)
            q.append(left_child)
        if right_index < len(values):
            right_child = HelperNode(values[right_index])
            to_proc.children.append(right_child)
            q.append(right_child)
        i += 1

    return root, nodes
    
