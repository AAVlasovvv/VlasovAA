def fact(N, depth=0):
    if N == 1:
        return 1
    print(depth)
    res = N*fact(N-1, depth+1)
    print(f'on step {depth} fact = {res}')
    return res
fact(5)