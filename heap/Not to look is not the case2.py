class Heap:
    def __init__(self):
        self._heap = []
    
    def _left(self, i):
        return 2 * i + 1
    
    def _right(self, i):
        return 2 * i + 2
    
    
    def _moving_up(self, i):
        while (i - 1) // 2 >= 0:
            parent_index = (i - 1) // 2
            if self._heap[i] < self._heap[parent_index]:
                self._heap[i], self._heap[parent_index] = self._heap[parent_index], self._heap[i]
            i = parent_index
    
    def add(self, item):
        if item in self._heap:
            return
        else:
            self._heap.append(item)
            self._moving_up(len(self._heap) - 1)
        
    def _moving_down(self, i):
        while 2*i+1 < len(self._heap):
            child = self._get_min_child(i)
            if self._heap[i] > self._heap[child]:
                self._heap[i], self._heap[child] = self._heap[child], self._heap[i]
            else:
                break
            i = child
    
    def _get_min_child(self, i):
        if 2*i+2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2 * i +2]:
            return 2 * i + 1
        return 2 * i+ 2
    
    # функция pop() вызывать так: heap.pop()
    def pop(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._moving_down(0)
        print(result)
        return
    
    def building_heap(self, array):
        self._heap = array[:]
        current_index = len(self._heap)//2 - 1
        while current_index >= 0:
            self._moving_down(current_index)
            current_index = current_index - 1
    
    # вызывать через print(): print(heap.heapsort(numbers))
    def heapsort(self, number):
        array = self._heap[number:]
        self._heap = array[:]
        self.sorting(self._heap, 0, len(array))
        # print(self._heap)

        current_index = len(self._heap) // 2 - 1
        while current_index >= 0:
            self._moving_down(current_index)
            current_index = current_index - 1

        print(self._heap)

        return self.__str__()
    
    def heapsort2(self, A):
        # создает приоритетную очередь и инициализирует ее заданным списком
        self._heap = A
        n = len(self._heap)
        # print(n)
        
        
        # Build-heap: вызывать heapify, начиная с последнего внутреннего
        # Узел # вплоть до корневого узла
        i = (n - 2) // 2
        while i >= 0:
            self.sorting(self._heap, i, n)
            i = i - 1
        
        # постоянно выталкивается из кучи, пока она не станет пустой
        while n:
            # print(self._heap)
            # print(n)
            self._heap[n-1] = self.delete(self._heap, n)
            n = n - 1
            
            
        print('Вывод списком:', *self._heap)
        print('Вывод деревом:')
        print(self.__str__())
        return
    
    def delete(self, A, size):
        
        # , если в куче нет элементов
        if size <= 0:
            return -1
        
        top = A[0]
        
        # заменить корень кучи последним элементом
        # списка
        A[0] = A[size - 1]
        
        # вызывает heapify-down на корневом узле
        self.sorting(A, 0, size - 1)
        
        return top
    
    def sorting(self, A, i, size):
    
        left = self._left(i)
        right = self._right(i)
        
        largest = i
        
        if left < size and A[left] > A[i]:
            largest = left
        
        if right < size and A[right] > A[largest]:
            largest = right
        
        if largest != i:
            A[i], A[largest] = A[largest],  A[i]
            self.sorting(A, largest, size)
    
    
    
    def get_root(self):
        return self._heap[0]
    
    def __len__(self):
        return len(self._heap)
    
    def get_child(self, index, side):
        if side == 'left':
            if index*2+1 <= len(self._heap):
                return self._heap[index*2+1]
            else:
                return None
        elif side == 'right':
            if index*2+2 <= len(self._heap):
                return self._heap[index*2+2]
            else:
                return None
        else:
            return ValueError
    
    
    def __str__(self):
        value_list = self._heap
        depth = 0
        counter = 0
        floor = []
        # print(value_list)
        for i in range(len(value_list)):
            counter += 1
            # print('c', counter)
            if value_list[i]:
                floor.append(value_list[i])
            # else:
            #     floor.append('None')
            
            if 2 ** depth == counter:
                counter %= (2 ** depth)
                # print('c%', counter)
                depth += 1
                # print('d', depth)
                print(*floor)
                floor = []
                continue
        print(*floor)
        return ''
    
heap = Heap()
heap.building_heap([9, 5, 6, 2, 3, 4, 7, 11, 10])
print(heap)
print(str(heap))
heap.add(4)
heap.add(84)
heap.add(12)
heap.add(13)
heap.add(14)
heap.add(15)
print(heap)
heap.pop()
print(heap)
heap.heapsort2([9, 5, 45, 2, 84, 4, 7, 62, 10])
print(heap.heapsort(3))
heap.add(47)
heap.add(78)
heap.add(1)
heap.add(12)
heap.add(3)
heap.add(99)
print(heap)



