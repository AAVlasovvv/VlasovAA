line = list(str(input()))
# print(stroka)
left_brackets = []
for i in range(0, len(line)):
    if line[i] == '(' or line[i] == '{' or line[i] == '[':
        left_brackets.append(line[i])
        # print(left_brackets)
    elif line[i] == ')' and left_brackets[-1] == '(':
        left_brackets.pop(-1)
        # print(left_brackets)
    elif line[i] == '}' and left_brackets[-1] == '{':
        left_brackets.pop(-1)
        # print(left_brackets)
    elif line[i] == ']' and left_brackets[-1] == '[':
        left_brackets.pop(-1)
        # print(left_brackets)

if len(left_brackets) == 0:
    print('Yes')
else:
    print('No')
    
 