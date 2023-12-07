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
        while 2 * i + 1 < len(self._heap):
            child = self._get_min_child(i)
            if self._heap[i] > self._heap[child]:
                self._heap[i], self._heap[child] = self._heap[child], self._heap[i]
            else:
                break
            i = child
    
    def _get_min_child(self, i):
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] < self._heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2
    
    
    def building_heap(self, array):
        self._heap = array[:]
        current_index = len(self._heap)//2 - 1
        while current_index >= 0:
            self._moving_down(current_index)
            current_index = current_index - 1
    
    def __len__(self):
        return len(self._heap)
    
    def get_child(self, index, side):
        if side == 'left':
            if index * 2 + 1 <= len(self._heap):
                return self._heap[index * 2 + 1]
            else:
                return None
        elif side == 'right':
            if index * 2 + 2 <= len(self._heap):
                return self._heap[index * 2 + 2]
            else:
                return None
        else:
            return ValueError
        

    def pop(self):
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._moving_down(0)
        return result
    
    
    def heapsort(self, number):
        array = self._heap[number:]
        self._heap = array[:]
        # self.sorting(self._heap, 0, len(array))
        # # print(self._heap)
        current_index = len(self._heap) // 2 - 1
        while current_index >= 0:
            self._moving_down(current_index)
            current_index = current_index - 1
        
        print('Вывод списком:', *self._heap)
        print('Вывод деревом:')
        print(self.__str__())
        return
    
    def __repr__(self):
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
heap.building_heap([9, 5, 6, 54, 13, 4, 7, 11, 10])
print(heap)
print(*heap._heap)
print('-'*100)
heap.add(4)
heap.add(1)
heap.add(12)
heap.add(19)
heap.add(2)
heap.add(15)
print(heap)
print(*heap._heap)
print('-'*100)
print(heap.pop())
print('-'*100)
print(heap)
print(*heap._heap)
print('-'*100)
heap.pop()
print(heap)
print(*heap._heap)
print('-'*100)
heap.heapsort(3)
print('-'*100)
