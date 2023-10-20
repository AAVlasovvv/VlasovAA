st = input()
st1 = st
L = len(st)
num_steps = L//2
flag = True
for i in range(num_steps):
    if st[i] != st[-i-1]:
        flag = False
        break
# print(1%2)
res1 = flag
# print(res1)
flag = True
res4 = False
if num_steps % 2 == 0:
    res4 = True
    for i in range(num_steps):
        if st[i] != st[-i - 1]:
            flag = False
            break
    res4 = flag



no_zamen = st.find('B' or 'C' or 'D' or 'F' or 'G' or 'K' or 'N' or 'P' or 'Q' or 'R' or '4' or '6' or '7' or '9')
if no_zamen == -1:
    flag = True
else:
    flag = False
res2 = flag
flag = True

# print(res2)

if res2 == True:
    st = st.replace('E', '3')
    st = st.replace('J', 'L')
    st = st.replace('S', '2')
    st = st.replace('Z', '5')
    for i in range(num_steps):
        if st[i] != st[-i-1]:
            flag = False
            break  
    res3 = flag
else:
    res3 = False
    
print(res1, res2, res3, res4)
if res1 == res2 == res3 == False:
    print(st1 + ' is not a palindrome.')
elif (res1 == True and res2 == res3 == False) or (res4 == True):
    print(st1 + ' is a regular palindrome.')
elif (res1 == False) and (res3 == res2 == True):
    print(st1 + ' is a mirrored string.')
elif res1 == res2 == res3 == True:
    print(st1 + ' is a mirrored palindrome.')



#print(res1)
#print(flag)
    #res = f'{st} palindrome = {flag}'
##for j in range(len(st)):
    #print(st[j])
    #if st[j] == 'C' or st[j] == 'D' or  st[j] == 'F' or  st[j] == 'G' or  st[j] == 'K' or  st[j] == 'N' or  st[j] == 'P' or  st[j] == 'Q' or  st[j] == 'R' or  st[j] == '4' or  st[j] == '6' or  st[j] == '7' or st[j] == '9':
        #flag = False
        #break
#print (flag)
#res2 = flag 





#print(res)