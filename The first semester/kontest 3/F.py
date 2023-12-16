
numbers= list(map(int, input().split()))
class Heap:
    def __init__(self):
        self._heap = []
    
    def heapify(self, array):
        self._heap = array[:]
        n = len(self._heap) // 2 - 1
        
        
        for i in range(n // 2 - 1, -1, -1):
            self._perc_up(i)
            
    def _perc_up(self, i):
        while 2 * i + 1 > 0:
            sm_child = self._get_max_child(i)
            print('sm_child',sm_child)
            if self._heap[i] < self._heap[sm_child]:
                self._heap[i], self._heap[sm_child] = self._heap[sm_child], self._heap[i]
            else:
                break
            i = sm_child
    
    def _get_max_child(self, i):
        if 2 * i + 2 > len(self._heap) - 1:
            return 2 * i + 1
        if self._heap[2 * i + 1] > self._heap[2 * i + 2]:
            return 2 * i + 1
        return 2 * i + 2
            
    
heap1 = Heap()
heap1.heapify(numbers)
print(heap1._heap)

