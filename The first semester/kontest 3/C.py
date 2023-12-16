N = int(input())
sections = []

Right =[]
Left = []
        
for i in range (N):
    sections = list(map(int, input().split()))
    
    R = sections[1]
    L = sections[0]
    Right.append(R)
    Left.append(L)
    
dictionary = dict(zip(Right, Left))

sort = []

import random

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)
sort = quicksort(Right)
res = 0
cur_res = 0
for i in range(N):
    Rmax = sort[i]
    for j in range(i,N):
        if Rmax < dictionary.get(sort[j]):
            Rmax = sort[j]
            cur_res += 1
        else:
            continue
    if cur_res >= res:
        res = cur_res
        
    cur_res = 0
        
print(res+1)
        
