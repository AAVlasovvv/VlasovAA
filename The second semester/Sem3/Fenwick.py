class FenwickTree:
    def __init__(self, data):
        self.data = data
        self.size = len(self.data)
        self.tree = [0] * self.size
        self.build_tree()
    
    def sum(self, index):
        result = 0
        while index >= 0:
            result += self.tree[index]
            index = (index & (index + 1)) - 1
        return result
    
    def range_sum(self, left, right):
        if left == right:
            return self.sum(right)
        else:
            return self.sum(right) - self.sum(left - 1)
    
    def build_tree(self):
        for i in range(self.size):
            delta = self.data[i]
            while i < self.size:
                self.tree[i] += delta
                i |= i + 1
        return self.tree
    
    def add(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index |= index + 1
    
    def update(self, index, new_value):
        delta = new_value - self.data[index]
        self.add(index, delta)
        self.data[index] = new_value


# Usage

fenwick_tree = FenwickTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

print(fenwick_tree.tree)
print(fenwick_tree.data)
print(fenwick_tree.sum(7))
print(fenwick_tree.range_sum(2, 5))
fenwick_tree.update(4, 10)
print(fenwick_tree.tree)
print(fenwick_tree.data)
print(fenwick_tree.sum(7))


        
