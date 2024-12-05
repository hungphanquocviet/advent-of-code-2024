import math
filepath = './day1/input.txt'

a = []
b = {}
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        x, y = map(int, line.strip().split())
        a.append(x)
        if y not in b:
            b[y] = 0
        
        b[y] += 1

a.sort()

res = 0
for i in range(len(a)):
    if a[i] not in b:
        continue
    res += a[i] * b[a[i]]

print(res)
