List = list(input().split())
# print(List)
error = 0
stack = []

for token in List:
    if token == '+':
        if -2 < -(len(stack)):
            # print('1')
            error += 1
            
        else:
            
            res = float(stack[-2]) + float(stack[-1])
            stack = stack[:-2]
            stack.append(res)
        
    elif token == '-':
        if -2 < -(len(stack)):
            # print('2')
            error += 1
            
        else:
            res = float(stack[-2]) - float(stack[-1])
            stack = stack[:-2]
            stack.append(res)
    elif token == '*':
        if -2 < -(len(stack)):
            # print('3')
            error += 1
            
        else:
            res = float(stack[-2]) * float(stack[-1])
            stack = stack[:-2]
            stack.append(res)
    elif token == '/':
        if -2 < -(len(stack)):
            # print('4')
            error += 1
            
        else:
            res = float(stack[-2]) / float(stack[-1])
            stack = stack[:-2]
            stack.append(res)
        
    elif token == '^':
        if -2 < -(len(stack)):
            print('5')
            error += 1
            
        else:
            res = float(stack[-2]) ** float(stack[-1])
            stack = stack[:-2]
            stack.append(res)
        
    else:
        stack.append(token)
        # print(stack)
    
if len(stack) != 1:
    error += 1

if error == 0:
    if float(stack[0])%1 == 0:
        print(int(stack[0]))
        
    if float(stack[0])%1 != 0:
        print(float(stack[0]))
else:
    print('Ja pierdolę, źle wpisałeś wyrażenie odwrotnej notacji polskiej... Popraw się, k***a!')
    

    