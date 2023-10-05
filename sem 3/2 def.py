# n = int(input())
# i = 2
# prostmn = []
# while i <= n:
#     if n % i == 0:
#         prostmn.append(i)
#         n = n / i
#     else:
#         i +=1
# print(prostmn)

def prostmn(i,num):
    if num == 1:
        return
    if num % i == 0:
        print(i)
        return prostmn(i, num//i)
         
    return prostmn(i+1, num)

num = int(input())
prostmn(2,num)
#mn = []
#print(mn)