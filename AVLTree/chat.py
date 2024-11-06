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
            # Base case: If the node is null, create a new node
            if node is None:
                return AVLTreeNode(key)

            # Recursive case: Insert in the left or right subtree
            if key < node.val:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)

            # Update height of this ancestor node
            self._update_height(node)

            # Get the balance factor to check if the node is unbalanced
            balance = self._balance_factor(node)

            # Left Left Case
            if balance > 1 and key < node.left.val:
                return self._rotate_right(node)

            # Right Right Case
            if balance < -1 and key > node.right.val:
                return self._rotate_left(node)

            # Left Right Case
            if balance > 1 and key > node.left.val:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            # Right Left Case
            if balance < -1 and key < node.right.val:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            # Return the unchanged node pointer
            return node

        # Call the recursive insert helper
        self.root = _insert(self.root, key)

    # Delete function
    def delete(self, key):
        def _delete(node, key):
            # Base case: if the node is not present
            if node is None:
                return node

            # Recursive case: Traverse to find the node
            if key < node.val:
                node.left = _delete(node.left, key)
            elif key > node.val:
                node.right = _delete(node.right, key)
            else:
                # Node with only one child or no child
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Node with two children: get the in-order successor
                temp = self._get_min_value_node(node.right)
                node.val = temp.val
                node.right = _delete(node.right, temp.val)

            # Update the height of the current node
            self._update_height(node)

            # Get the balance factor to check if the node is unbalanced
            balance = self._balance_factor(node)

            # Left Left Case
            if balance > 1 and self._balance_factor(node.left) >= 0:
                return self._rotate_right(node)

            # Left Right Case
            if balance > 1 and self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            # Right Right Case
            if balance < -1 and self._balance_factor(node.right) <= 0:
                return self._rotate_left(node)

            # Right Left Case
            if balance < -1 and self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

            return node

        self.root = _delete(self.root, key)

    # Helper function to find the node with the minimum value
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