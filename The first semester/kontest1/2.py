gear = list(map(int, input().split()))
a = int(gear[0])
b = int(gear[1])
x = 0
while ((a+x)%b) != ((b+x)%a):
    x += 1
print(x)

