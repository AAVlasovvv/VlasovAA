examples = []
lines = True
while lines != '0 0':
    lines = input()
    if lines: examples.append(lines)

examples.pop(-1)
# print(len(examples))
howmanywas = []
for i in range(0, len(examples), 2):
    howmanywas.append(((examples[i].split())[0]))
    
howmanywas1 = list(map(int, howmanywas))
print(howmanywas1)


howmucharewedeleting = []
for i in range(0, len(examples), 2):
    howmucharewedeleting.append(((examples[i].split())[1]))
    
howmucharewedeleting1 = list(map(int, howmucharewedeleting))
print(howmucharewedeleting1)



fromwhatwedelete = []
for i in range(1, len(examples), 2):
    fromwhatwedelete.append((examples[i]))
fromwhatwedelete1 = list(map(int, fromwhatwedelete))
# print(type(fromwhatwedelete1[1]))

result = []

for i in range(0, int(len(examples)/2)):
    N = howmucharewedeleting1[i]
    print(N)
    work = [int(i) for i in str(fromwhatwedelete[i])]
    print(work)
    result.append(work[0])
    print(result)
    for j in range(0, len(work)):
        while result and N > 0 and work[j] > int(result[-1]):
            result.pop()
            N -= 1
        result.append(str(work[j]))
    print(''.join(result))
    result = []
            
    

