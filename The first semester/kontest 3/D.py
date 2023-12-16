N , R = map(int,input().split())
villages= list(map(int, input().split()))

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

villages = quicksort(villages)
# print(villages)

res = 0
k = 0
n = 0
# print(len(villages))
while k <= (len(villages)-1):
    if villages[k] - villages[n] > 2*R:
        villages = villages[k-1:]
        res += 1
        k = 0
    else:
        k += 1
        continue
    
print(res)
    

