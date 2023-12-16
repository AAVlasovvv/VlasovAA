N , L = map(int,input().split())
articles = list(map(int, input().split()))

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

articles = quicksort(articles)

# print(articles)
if L > 0:
    for i in range(L):
        articles[i] += 1
        
# print(articles)

def find_h(array):
    minus = 0
    h = 0
    while h == 0:
        if array[0+minus] >= len(array)-minus:
            h = len(array)-minus
            return h
        else:
            minus += 1
            continue
            
print(find_h(articles))
            

