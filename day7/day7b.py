filepath = './day7/input.txt'

content = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        parts = line.split(':')
        numbers = list(map(int, parts[1].strip().split()))
        
        content.append((parts[0], numbers))

def dp(nums, target, current, i, memo):
    if current == target and i == len(nums):
        return True
    
    if i >= len(nums):
        return False
    
    if (current, i) in memo:
        return memo[(current, i)]
    
    add = dp(nums, target, current + nums[i], i+1, memo)
    mul = dp(nums, target, current * nums[i], i+1, memo)
    concat = dp(nums, target, int(str(current) + str(nums[i])), i+1, memo)
    
    memo[(current, i)] = add or mul or concat
    return memo[(current, i)]

res = 0
for c in content:
    target = int(c[0])
    nums = c[1]
    memo = {}
    
    valid = dp(nums, target, nums[0], 1, memo)
    res += target if valid else 0

print(res)
    


