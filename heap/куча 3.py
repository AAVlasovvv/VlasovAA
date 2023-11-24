class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._insert_helper(self.root, val)

    def _insert_helper(self, node, val):
        if not node.left:
            node.left = Node(val)
        elif not node.right:
            node.right = Node(val)
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)

            if left_height <= right_height:
                self._insert_helper(node.left, val)
            else:
                self._insert_helper(node.right, val)

        self._heapify_up(node)

    def _heapify_up(self, node):
        if node and node.val < node.parent.val:
            node.val, node.parent.val = node.parent.val, node.val
            self._heapify_up(node.parent)

    def extract_min(self):
        if not self.root:
            return None

        min_val = self.root.val

        bottom_right_node = self._get_bottom_right_node()
        if bottom_right_node:
            self.root.val = bottom_right_node.val
            self._delete_bottom_right_node()
            self._heapify_down(self.root)

        return min_val

    def _get_bottom_right_node(self):
        level = self._get_height(self.root)
        return self._get_bottom_right_node_helper(self.root, level)

    def _get_bottom_right_node_helper(self, node, level):
        if not node:
            return None

        if level == 1:
            return node

        left_node = self._get_bottom_right_node_helper(node.left, level - 1)
        right_node = self._get_bottom_right_node_helper(node.right, level - 1)

        if right_node:
            return right_node
        return left_node

    def _delete_bottom_right_node(self):
        level = self._get_height(self.root)
        self._delete_bottom_right_node_helper(self.root, level)

    def _delete_bottom_right_node_helper(self, node, level):
        if not node:
            return

        if level == 1:
            node = None
            return

        self._delete_bottom_right_node_helper(node.left, level - 1)
        self._delete_bottom_right_node_helper(node.right, level - 1)

    def _heapify_down(self, node):
        if not node:
            return

        smallest = node
        if node.left and node.left.val < smallest.val:
            smallest = node.left

        if node.right and node.right.val < smallest.val:
            smallest = node.right

        if smallest != node:
            node.val, smallest.val = smallest.val, node.val
            self._heapify_down(smallest)

    def _get_height(self, node):
        if not node:
            return 0

        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)

        return max(left_height, right_height) + 1
    
    def __repr__(heap):
        """
        Выводит кучу по этажам.
        Аргументы:
        - heap: список с элементами кучи.
        """
        level = 1
        level_nodes = 1
        nodes_printed = 0
        
        for node in heap:
            print(node, end=" ")
            nodes_printed += 1
            
            if nodes_printed == level_nodes:
                print("\n")
                level += 1
                level_nodes *= 2
                nodes_printed = 0


# Пример использования

heap = MinHeap()
heap.insert(1)
heap.insert(2)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(9)
heap.insert(10)
heap.insert(11)
print(heap)


# print(heap.extract_min())  # Output: 1
# print(heap.extract_min())  # Output: 2
# print(heap.extract_min())  # Output: 3
# print(heap.extract_min())  # Output: 5
# print(heap.extract_min())  # Output: 8
