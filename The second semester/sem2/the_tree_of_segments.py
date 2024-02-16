import numpy as np

class SumTree:
    
    def __init__(self, data: list):
        ln = len(data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = data
        else:
            self.data = data
            lb = int(lb) + 1
            for i in range(ln, 2**lb):
                self.data.append(0)
                
        self.tree = [0 for i in range(len(self.data)-1)] + self.data
        self.calc_tree()
        
    def calc_tree(self) -> None:
        for i in range(len(self.tree)+1, 2, -2):
            s1 = self.tree[i-2]
            s2 = self.tree[i-3]
            sm = s1 + s2
            self.tree[(i-4)//2] = sm
            

def Sum(tree, l:int, r:int):
    def tree_sum(l:int, r:int, tl=0, tr = len(tree.data) - 1):
        
        root = tree.tree[0]
        #left from root - [0,(len(data))//2]
        #right from root - [(len(self.data))//2,len(self.data)]
        sum = 0
        if l <= tl and r >= tr:
            
            index1 = len(tree.data) + tr - 1
            index2 = len(tree.data) + tl
            while index1 != index2:
                index1 = max((index1-2)//2, 0)
                index2 = max((index2-2)//2, 0)
            
            return tree.tree[index1]
        
        if tl == tr:
            return tree.data[tl]
        
        tm = (tl + tr) // 2
        if tm == tl:
            return tree.data[tm]
        go_left = l < tm
        go_right = r >= tm
        

        if go_left:
            sum += tree_sum(tree, l, tm-1, tl = tl, tr = tm-1)
        if go_right:
            sum += tree_sum(tree, tm, r, tl = tm, tr = tr)
    
    return tree_sum(l, r)
        
            
            
            
        
            
        
                
                
    

tree = SumTree([1,2,3,4,5,6,7,8,9])
print(tree.tree)


        
            
            
        
    
     
    # def sun(self) -> int:
    