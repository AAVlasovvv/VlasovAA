def find_combinations(arr, target):
    def helper(arr, target, index, memo):
        if target == 0:
            return 1
        if target < 0 or index >= len(arr):
            return 0
        if (index, target) in memo:
            return memo[(index, target)]
        
        count = 0
        count += helper(arr, target - arr[index], index, memo)
        count += helper(arr, target, index + 1, memo)
        
        memo[(index, target)] = count
        return count
    
    memo = {}
    return helper(arr, target, 0, memo)


arr = [2, 4, 6]
target = 6
num_combinations = find_combinations(arr, target)
print("Number of combinations:", num_combinations)

