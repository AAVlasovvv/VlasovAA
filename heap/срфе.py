import math
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, element):
        self.heap.append(element)
        current_index = len(self.heap) - 1

        while (
            current_index > 0
            and self.heap[current_index] < self.heap[self.parent(current_index)]
        ):
            parent_index = self.parent(current_index)
            self.swap(current_index, parent_index)
            current_index = parent_index

    def heapify_down(self, i):
        left_index = self.left_child(i)
        right_index = self.right_child(i)
        smallest = i

        if (
            left_index < len(self.heap)
            and self.heap[left_index] < self.heap[smallest]
        ):
            smallest = left_index

        if (
            right_index < len(self.heap)
            and self.heap[right_index] < self.heap[smallest]
        ):
            smallest = right_index

        if smallest != i:
            self.swap(i, smallest)
            self.heapify_down(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        min_element = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify_down(0)

        return min_element

    def display_heap(self):
        """
        Выводит содержимое бинарной кучи.
        """
        if len(self) == 0:
            print("Куча пуста.")
        else:
            # Определяем количество уровней в куче
            levels = int(math.log2(len(self))) + 1
    
            # Определяем индексы элементов на каждом уровне
            level_indices = [2 ** level - 1 for level in range(levels)]
    
            # Определяем максимальное значение в куче, чтобы правильно выравнивать элементы
            max_value = max(self)
    
            # Выводим элементы кучи
            for level in range(levels):
                indices = range(level_indices[level], min(len(heap), level_indices[level+1]))
                for index in indices:
                    element = self[index]
                    spaces = " " * (len(str(max_value)) - len(str(element)))
                    print(spaces, element, end=" ")
                print()
                
heap1 = MinHeap([])
heap1.heap = [4, 9, 7, 1, 3, 6, 5]

display_heap(heap1)