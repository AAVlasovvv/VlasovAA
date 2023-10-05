n = int(input())
i = 2
prostmn = []
while i <= n:
    if n % i == 0:
        prostmn.append(i)
        n = n / i
    else:
        i +=1
print(prostmn)