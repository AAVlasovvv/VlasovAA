def triygol(size, symb):
    for i in range(1, size + 1):
        minimum = min(i, size - i + 1)
        #print(minimum)
        print(symb * minimum)

data = list(input().split())
#print(data)
size, symb = int(data[0]), str(data[1])
triygol(size, symb)