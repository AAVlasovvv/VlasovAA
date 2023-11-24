class Heap:
    class Node:
        def __init__(self, value, left=None, right=None, index=None):
            self.left = left
            self.right = right
            self.value = value
            self.index = index
        
        def __repr__(self):
            value_list = self.listing()
            depth = 0
            counter = 0
            floor = []
            print(value_list)
            for i in range(len(value_list)):
                counter += 1
                if value_list[i]:
                    floor.append(value_list[i])
                else:
                    floor.append(None)
                
                if 2 ** depth == counter:
                    counter %= (2 ** depth)
                    depth += 1
                    print(*floor)
                    floor = []
                    continue
            
            return ''
        
        def listing(self) -> list:
            nodes_list = []
            
            if self.left:
                nodes_list.append(self.left)
                # print(nodes_list)
            if self.right:
                nodes_list.append(self.right)
                # print(nodes_list)
            
            for node in nodes_list:
                if not node:
                    continue
                if node.left:
                    nodes_list.append(node.left)
                else:
                    nodes_list.append(None)
                if node.right:
                    nodes_list.append(node.right)
                else:
                    nodes_list.append(None)
            value_list = [self.value]
            for node in nodes_list:
                if node:
                    value_list.append(node.value)
                else:
                    value_list.append(None)
            
            return value_list
        
        def get_value(self):
            return self.value
        
        def get_child(self, side='left'):
            if side == 'left':
                return self.left
            elif side == 'right':
                return self.right
            else:
                return ValueError
        
        def set_child(self, node, side='left'):
            if side == 'left':
                self.left = node
                return
            elif side == 'right':
                self.right = node
                return
            else:
                return ValueError
    
    # def __init__(self):
    #     self.root = None
    #     self.heap = []
    #
    # def get_root(self):
    #     return self.root
    #
    # def add(self, num):
    #     assert isinstance(num, int)
    #     node = self.Node(num)
    #     if not self.root:
    #         self.root = node
    #         return
    #     current_node = self.root
    #     up_node = None
    #     while node.value > current_node.value:
    #         if not current_node.left:
    #             current_node.left = node
    #             return
    #         elif not current_node.right:
    #             current_node.right = node
    #             return
    #         up_node = current_node
    #         current_node = current_node.left
    #     if up_node:
    #         up_node.left = node
    #     node.left = current_node.left
    #     current_node.left = None
    #     node.right = current_node
    #     return
    #
    # def pop(self) -> int:  # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ
    #     return 0
    #
    # def heapsort(self) -> list:  # НАПИСАТЬ УДАЛЕНИЕ КОРНЯ N раз (построенная пирамида выводит упорядоченный список)
    #     return 0
    

    def __init__(self):
        # Инициализация пустой кучи
        self.heap = []
        self.root = None
        self.index = 0

    def parent(self, index):
        # Вычисление индекса родительского узла
        return (index - 1) // 2

    def left_child(self, index):
        # Вычисление индекса левого потомка
        return (2 * index) + 1

    def right_child(self, index):
        # Вычисление индекса правого потомка
        return (2 * index) + 2

    def swap(self, i, j):
        # Обмен значений элементов с индексами i и j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def add(self, num):
        assert isinstance(num, int)
        node = self.Node(num)
        self.heap[self.index] = node.value
        node.index = self.index
        self.index += 1
        self._siftup(self.index - 1)
        
    def _siftup(self, index):
        """
        To keep the the attribute of heap unchanged while adding a new value.
        :param index: the index of value you want to swap
        :return: None
        """
        if index > 0:
            parent = int((index - 1) / 2)
            if self.heap[parent] > self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                self._siftup(parent)
    
    def extract(self):
        # value = self.Node()
        if self.index <= 0:
            raise Exception('The heap is empty!')
        value = self.heap[0]
        self.index -= 1
        self.heap[0] = self.heap[self.index]
        self._siftdown(0)
        return value
    
    def _siftdown(self, index_):
        """
        to keep the attribute of heap unchanged while pop out the root node.
        :param index: the index of value you want to swap
        :return: None
        """
        if index_ < self.index:
            left = 2 * index_ + 1
            right = 2 * index_ + 2
            if left < self.index and right < self.index and self.heap[left] <= self.heap[right] and self.heap[left] <= self.heap[index_]:
                self.heap[left], self.heap[index_] = self.heap[index_], self.heap[left]
                self._siftdown(left)
            elif left < self.index and right < self.index and self.heap[left] >= self.heap[right] and self.heap[right] <= self.heap[index_]:
                self.heap[right], self.heap[index_] = self.heap[index_], self.heap[right]
                self._siftdown(left)

            if left < self.index and right > self.index and self.heap[left] <= self.heap[index_]:
                self.heap[left], self.heap[index_] = self.heap[index_], self.heap[left]
                self._siftdown(left)
                
    # def insert(self, item):
    #     # Вставка нового элемента в кучу
    #     self.heap.append(item)
    #     current_index = len(self.heap) - 1
    #
    #     while current_index > 0:
    #         parent_index = self.parent(current_index)
    #         if self.heap[current_index] < self.heap[parent_index]:
    #             # Если текущий элемент меньше его родительского узла,
    #             # меняем их местами
    #             self.swap(current_index, parent_index)
    #             current_index = parent_index
    #         else:
    #             # В противном случае, куча восстановлена
    #             break
    #
    # def extract_min(self):
    #     # Извлечение минимального элемента из кучи
    #     if len(self.heap) == 0:
    #         raise IndexError("Heap is empty")
    #
    #     min_element = self.heap[0]
    #     last_element = self.heap.pop()
    #     if len(self.heap) > 0:
    #         # Если куча не пустая, заменяем удаленный элемент
    #         # на последний элемент и восстанавливаем свойство кучи
    #         self.heap[0] = last_element
    #         self._heapify(0)
    #
    #     return min_element
    #
    # def _heapify(self, index):
    #     # Восстановление свойства кучи с корневым узлом index
    #     left = self.left_child(index)
    #     right = self.right_child(index)
    #     smallest = index
    #
    #     # Сравниваем корневой узел с левым потомком
    #     if left < len(self.heap) and self.heap[left] < self.heap[index]:
    #         smallest = left
    #
    #     # Сравниваем корневой узел с правым потомком
    #     if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
    #         smallest = right
    #
    #     if smallest != index:
    #         # Если корневой узел не является наименьшим, меняем его местами
    #         # с наименьшим потомком и рекурсивно вызываем _heapify для потомка
    #         self.swap(index, smallest)
    #         self._heapify(smallest)


heap = Heap()

'''
first_node = Node(5)
second_node = Node(4)
third_node = Node(3)
quatro_node = Node(1)
cinco_node = Node(2)
seis_node = Node(10)
siete_node = Node(6)
ocho_node = Node(0)

heap.add(first_node)
heap.add(second_node)
heap.add(third_node)
heap.add(quatro_node)
heap.add(cinco_node)
heap.add(seis_node)
heap.add(siete_node)
heap.add(ocho_node)
#print(quattro_node.listing())
#print(third_node.listing())
print(heap.get_root())
'''
heap.add(1)
heap.add(2)
heap.add(3)
heap.add(4)
heap.add(5)
heap.add(6)
heap.add(7)
heap.add(8)
heap.add(10)
heap.add(11)
heap.add(9)
heap.add(12)
heap.add(13)
heap.add(14)
heap.add(15)
heap.add(15)
heap.add(15)
print(heap)