f1 = open('input9.txt', 'r')
L2 = f1.read()
#print(L2)
L1 = list(L2)
#print(L1)
chet = 0
for i in range (len(L1)-2):
    #print(L1[i])
    if (L1[i] == '.' or L1[i] == '!' or L1[i] == '?') and L1[i+1] == ' ':
        chet = chet + 1
#if L1[-1] == ' ':
    #print(chet)
#else:
    #print(chet + 1)

print(chet + 1)