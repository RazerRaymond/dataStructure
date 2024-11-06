from AVLTree.AVLTree import AVLTreeNode


class AVLTreeChat:
    def __init__(self):
        self.root = None

    # Helper function to calculate the height of a node
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # Helper function to update the height of a node
    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))

    # Helper function to calculate the balance factor of a node
    def _balance_factor(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    # Right rotation to maintain balance
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        # Return new root
        return x

    # Left rotation to maintain balance
    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        self._update_height(x)
        self._update_height(y)

        # Return new root
        return y

    # Insert function
    def insert(self, key):
        def _insert(node, key):
            if node is None:
                return AVLTreeNode(key)

            if key < node.val:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            self._update_height(node)

            balance = self._balance_factor(node)

            if balance > 1 and key < node.left.val:
                return self._rotate_right(node)

            if balance < -1 and key > node.right.val:
                return self._rotate_left(node)

            if balance > 1 and key > node.left.val:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            if balance < -1 and key < node.right.val:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return node

        self.root = _insert(self.root, key)

    # Delete function
    def delete(self, key):
        def _delete(node, key):
            if node is None:
                return node

            if key < node.val:
                node.left = _delete(node.left, key)
            elif key > node.val:
                node.right = _delete(node.right, key)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self._get_min_value_node(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)

            self._update_height(node)

            balance = self._balance_factor(node)

            if balance > 1 and self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)

            if balance > 1 and self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            if balance < -1 and self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)

            if balance < -1 and self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return node

        self.root = _delete(self.root, key)

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Search function
    def search(self, key):
        def _search(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return _search(node.left, key)
            return _search(node.right, key)

        return _search(self.root, key)

    # Function to print the tree (in-order traversal)
    def in_order(self):
        def _in_order(node):
            if node:
                print(node.val, end=' | ')
                _in_order(node.left)
                _in_order(node.right)

        _in_order(self.root)
        print()