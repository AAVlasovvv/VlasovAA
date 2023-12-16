def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1    
    right = 2 * i + 2    

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  
        heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


array = list(map(int, input().split()))
build_max_heap(array)
print(*array)