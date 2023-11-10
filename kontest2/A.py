N = int(input())
coordinates = []
newdistance = float()
olddistance = float()
res = False
for i in range(N):
    coordinates.append(list(map(int, input().split())))
# print(coordinates)
if coordinates[0][1] == coordinates[-1][1]:
    olddistance = (int(coordinates[0][0])+int(coordinates[-1][0]))/2
    for i in range(1,N):
        if coordinates[i][1] == coordinates[-1-i][1]:
            newdistance = (int(coordinates[i][0])+int(coordinates[-1-i][0]))/2
            if newdistance == olddistance:
                res = True
            else:
                res = False
                break
        else:
            break
            
if res == True:
    print('Yes')
else:
    print('No')

            