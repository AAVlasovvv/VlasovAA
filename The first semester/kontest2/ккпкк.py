def count_combinations(N):
    dp = [0] * (N + 1)
    dp[0] = 1  # Один способ получить стопку размером 0 - не использовать ни одного блока

    for i in range(1, N + 1):
        for j in [1, 2, 3]:
            if i-j >= 0:
                dp[i] += dp[i - j]

    return dp

# Чтение входных данных
stack_sizes = []
while True:
    size = int(input())
    if size == 0:
        break
    stack_sizes.append(size)

# Вычисление и вывод результатов
combinations = count_combinations(max(stack_sizes))
for size in stack_sizes:
    print(combinations[size])



