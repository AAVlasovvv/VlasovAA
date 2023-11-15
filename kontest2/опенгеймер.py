def calculate_output(stacks):
    output = [0, 1, 3]
    for stack in stacks:
        if stack <= 2:
            print(0)
        elif stack == 3:
            print(1)
        else:
            for j in range(5, stack + 1):
                output.append(2**(j - 3) + output[-1] + output[-2] + output[-3])
            print(output[stack - 2])
        output = [0, 1, 3]

def get_input():
    stacks_list = []
    while True:
        stack = input()
        if stack == '0':
            break
        stacks_list.append(int(stack))
    return stacks_list

def main():
    stacks = get_input()
    calculate_output(stacks)

if __name__ == "__main__":
    main()
