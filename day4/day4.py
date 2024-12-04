filepath = './day4/input.txt'

a = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        a.append(line.strip())

r = len(a)
c = len(a[0])

def search(arr, s, i, j, dirs):
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]):
        return 0
     
    s += arr[i][j]
    if len(s) > 4:
        return 0
    
    if len(s) == 4 and s == 'XMAS':
        return 1
    return search(arr, s, i + dirs[0], j + dirs[1], dirs)
res = 0

directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
for i in range(r):
    for j in range(c):
        if a[i][j] == 'X':
            for dirs in directions:
                res += search(a, '', i, j, dirs)
                
print(res)