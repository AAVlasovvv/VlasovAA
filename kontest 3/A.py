nums = list(map(int, input().split()))
print(nums)

def sorting(nums):
    if len(nums) <= 1:
        print(nums + ' pierdolę, wpisałeś tablicę tożsamości, nie można jej sortować')
        return
    else:
    