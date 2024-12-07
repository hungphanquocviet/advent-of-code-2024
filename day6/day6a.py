filepath = './day6/sample.txt'

content = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        temp = list(line.strip())
        content.append(temp)
        

r = 0
c = 0

m = len(content)
n = len(content[0])

found = False
for i in range(m):
    for j in range(n):
        if content[i][j] == '^':
            found = True
            r, c = i, j
            break
        
    if found:
        break
    
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

cnt = 0
path_end = False
d = 2

visited = set()
while 0 <= r < m and 0 <= c < n:
    dr = r + dirs[d][0]
    dc = c + dirs[d][1]
    
    if 0 <= dr < m and 0 <= dc < n and content[dr][dc] == '#':
        d = (d + 1) % 4
    
    else:
        
        if 0 <= r < m and 0 <= c < n:
            
            visited.add((r, c))
            content[r][c] = 'X'
            r = dr
            c = dc
        

print(len(visited))

