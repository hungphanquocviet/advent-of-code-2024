import math
#filepath = './day1/input.txt'
filepath = './day1/sample.txt'

a = []
b = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        x, y = map(int, line.strip().split())
        a.append(x)
        b.append(y)

a.sort()
b.sort()

res = 0
for i in range(len(a)):
    res += abs(a[i] - b[i])

print(res)
