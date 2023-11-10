examples = []
lines = True
while lines != '0 0':
    lines = input()
    if lines: examples.append(lines)

examples.pop(-1)
howmucharewedeleting = []
for i in range(0, len(examples), 2):
    howmucharewedeleting.append(examples[i].split())
# print(howmucharewedeleting)

fromwhatwedelete = []
for i in range(1, len(examples), 2):
    fromwhatwedelete.append(examples[i])

# print(len(howmucharewedeleting))
result = []

for k in range(0, len(howmucharewedeleting)):
    for i in range(0, int(howmucharewedeleting[k][1])):
        # print(howmucharewedeleting[k][1])
        min_digit=min(str(fromwhatwedelete[k]))
        # result = fromwhatwedelete[k].replace(min_digit, '', 1)
        fromwhatwedelete[k] = fromwhatwedelete[k].replace(min_digit, '', 1)
        # print(fromwhatwedelete[k])
        result = fromwhatwedelete[k]
    print(result)
    result=[]






