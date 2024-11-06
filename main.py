from AVLTree.AVLTree import AVLTree
from AVLTree.chat import AVLTreeChat

if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree_example = AVLTreeChat()
    nodes_to_insert = [40, 20, 10, 25, 30, 22, 50, 21, 23, 26, 31, 45, 55, 1]
    for node in nodes_to_insert:
        avl_tree.insert(node)
        avl_tree_example.insert(node)

    avl_tree.delete(10)
    avl_tree.print_avl_tree()
    print()
    avl_tree_example.delete(10)
    avl_tree_example.in_order()