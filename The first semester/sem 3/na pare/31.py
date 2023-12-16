def euclid(a,b):
    if a == 0:
        return b, 0, 1
    d, u, v = euclid(b % a, a)
    print(d, u, v)
    x = v - (b // a ) * u
    print(x)
    y = u
    print(y)
    return d, x, y

a, b = map(int, input().split(" "))
print(euclid(a,b))
