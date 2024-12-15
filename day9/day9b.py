from collections import defaultdict, deque
filepath = './day9/input.txt'

s = ''
with open(filepath, encoding='utf8') as file:
    s = file.readline()

s_list = list(s)
id = 0

a = ''
for ind, c in enumerate(s_list):
    if ind % 2 == 0:
        length = int(c)
        for _ in range(length):
            a += str(id)
        id += 1
    else:
        length = int(c)
        for _ in range(length):
            a += '.'
a = list(a)

l = 0
r = len(a) - 1

while l < r:
    while a[l] != '.':
        l += 1

    while a[r] == '.':
        r -= 1
    
    temp = a[r]
    a[r] = a[l]
    a[l] = temp
    
    l += 1
    r -= 1
    #print(''.join(a))

ans = 0
print(a)
for i, val in enumerate(a):
    if a[i] != '.':
        ans += i * int(val)

print(ans)