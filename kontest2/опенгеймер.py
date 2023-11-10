stacks = []
stacks_p = True
while stacks_p != '0':
    stacks_p = input()
    if stacks_p: stacks.append(int(stacks_p))

stacks.pop(-1)
output = [0, 1, 3]
for i in range(len(stacks)):
    if stacks[i] <= 2:
        print(0)
    elif stacks[i] == 3:
        print(1)
    else:
        for j in range(5, stacks[i] + 1):
            output.append(2**(j - 3) + output[-1] + output[-2] + output[-3])
        print(output[stacks[i] -2])
        output = [0, 1, 3]
