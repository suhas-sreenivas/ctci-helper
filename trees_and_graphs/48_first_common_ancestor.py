from helpers.helper import *
from helpers.pptree import *

def first_common_ancestor(root, node1, node2):
    if root == None or root == node1 or root == node2:
        return root
    
    try:
        x = first_common_ancestor(root.children[0], node1, node2)
    except IndexError:
        x = None
    if x is not None and x is not node1 and x is not node2: #common ancestor already found
        return x
    
    try:
        y = first_common_ancestor(root.children[1], node1, node2)
    except IndexError:
        y = None
        
    if y is not None and y is not node1 and y is not node2: #common ancestor already found
        return y

    if x is not None and y is not None: # nodes found in diff subtrees, so this is the common ancestor, bubble it up
        return root
    elif root is node1 or root is node2: 
        return root
    else:
        return x if y is None else y # bubble up None or one of the nodes found

if __name__ == "__main__":
    values = [20, 10, 30, 5, 15, None, None, 3, 7, None, 17]
    root, nodes = construct_binary_tree(values)
    print_tree(root)
    print(first_common_ancestor(root, nodes[7], nodes[17]).data)
