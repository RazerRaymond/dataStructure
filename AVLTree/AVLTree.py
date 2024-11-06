from shared import TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, val=None, left=None, right=None):
        super().__init__(val=val,
                         left=left,
                         right=right)
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
    def _rotate_right(self, node):
        L = node.left
        move_part = L.right

        L.right = node
        node.left = move_part

        self.__update_height(node)
        self.__update_height(L)

        return L

    def _rotate_left(self, node):
        R = node.right
        move_part = R.left

        R.left = node
        node.right = move_part

        self.__update_height(node)
        self.__update_height(R)

        return R

    def insert(self, val):
        def _insert_helper(node: AVLTreeNode, val):
            if node is None:
                return AVLTreeNode(val=val)
            if node.val > val:
                node.left = _insert_helper(node.left, val)
            else:
                node.right = _insert_helper(node.right, val)

            self.__update_height(node)
            current_balance_factor = self.__calculate_balance_factor(node)

            if current_balance_factor > 1 and val < node.left.val:
                return self._rotate_right(node)

            elif current_balance_factor > 1 and val > node.left.val:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            elif current_balance_factor < -1 and val > node.right.val:
                return self._rotate_left(node)

            elif current_balance_factor < -1 and val < node.right.val:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            else:
                return node

        self.root = _insert_helper(self.root, val)

    def delete(self, val):
        def _delete_helper(node: AVLTreeNode, val):
            if node is None:
                return None

            if node.val > val:
                node.left = _delete_helper(node.left, val)
            elif node.val < val:
                node.right = _delete_helper(node.right, val)
            else:
                # Found the element, start deleting
                if node.left is None:
                    node = node.right
                elif node.right is None:
                    node = node.left
                else:
                    tmp = self.__find_max_element(node.left)
                    node.key = tmp.key
                    node = _delete_helper(node.left, tmp.key)

            self.__update_height(node)
            current_balance_factor = self.__calculate_balance_factor(node)

            if current_balance_factor > 1 and self.__calculate_balance_factor(node.left) >= 0:
                return self._rotate_right(node)

            elif current_balance_factor > 1 and self.__calculate_balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

            elif current_balance_factor < -1 and self.__calculate_balance_factor(node.right) <= 0:
                return self._rotate_left(node)

            elif current_balance_factor < -1 and self.__calculate_balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
            else:
                return node
        self.root = _delete_helper(self.root, val)

    def print_avl_tree(self):
        def _print_helper(node):
            if node is None:
                return
            print(node.val, end=" | ")
            _print_helper(node.left)
            _print_helper(node.right)
        _print_helper(self.root)

# --------------------------Internal Methods--------------------------
    def __get_height(self, node: AVLTreeNode):
        if node is None:
            return 0
        return node.height

    def __update_height(self, node: AVLTreeNode):
        if node is not None:
            node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1

    def __calculate_balance_factor(self, node: AVLTreeNode):
        if node is None:
            return 0
        return self.__get_height(node.left) - self.__get_height(node.right)

    def __find_max_element(self, root: AVLTreeNode):
        cur_node = root
        while root.right is not None:
            cur_node = cur_node.right
        return cur_node
