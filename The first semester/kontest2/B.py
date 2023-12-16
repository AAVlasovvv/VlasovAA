stacks = []
stacks_p = True
while stacks_p != '0':
    stacks_p = input()
    if stacks_p: stacks.append(stacks_p)

stacks.pop(-1)

# print(stacks)

number_of_dangerous_combinations = 0

# table = []
element = 0
for i in range(0, len(stacks)):
    # table = [[] for _ in range(2**(int(stacks[i])))]
    # print(table)
    for k in range(0, 2**(int(stacks[i]))):
        meaning = bin(k)
        element = str((f'{int(meaning[2:]):0{int(stacks[i])}}'))
        if '000' in element:
            number_of_dangerous_combinations += 1
    
    print(number_of_dangerous_combinations)
    number_of_dangerous_combinations = 0