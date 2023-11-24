class MinHeap:
    def __init__(self):
        self.heap = []


    def insert(self, value):
        self.heap.append(value)
        self._upheap()
    
    
    def remove_min(self):
        if not self.heap:
            return None
    
    
        self._swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self._downheap()
        
        return min_value
    
    
    def heapify(self, values):
        self.heap = values
    
    
        for i in range(len(self.heap) // 2, -1, -1):
            self._downheap(i)
    
    
    def _upheap(self):
        index = len(self.heap) - 1
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2
    
    
    def _downheap(self, index=0):
        child_index = 2 * index + 1
        while child_index < len(self.heap):
            if child_index + 1 < len(self.heap) and self.heap[child_index + 1] < self.heap[child_index]:
                child_index += 1
            
            if self.heap[index] <= self.heap[child_index]:
                break
            
            self._swap(index, child_index)
            index = child_index
            child_index = 2 * index + 1
    
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


# Создание экземпляра класса и вставка элементов
heap = MinHeap()
heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(2)
heap.insert(10)

# Удаление минимального элемента из кучи
min_value = heap.remove_min()
print(min_value)  # Выводит 2

# Приведение списка к минимальной куче
values = [9, 5, 2, 8, 4]
heap.heapify(values)
print(heap)