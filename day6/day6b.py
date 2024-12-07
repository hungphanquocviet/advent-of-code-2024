filepath = './day6/input.txt'

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

def good(sr, sc, obr, obc):
    visited = set()
    r, c = sr, sc
    d = 2  
    while 0 <= r < m and 0 <= c < n:
        state = (r, c, d)
        if state in visited:
            return True
        visited.add(state)

        dr, dc = r + dirs[d][0], c + dirs[d][1]

        if (dr, dc) == (obr, obc) or (0 <= dr < m and 0 <= dc < n and content[dr][dc] == '#'):
            d = (d + 1) % 4
        else:
            r, c = dr, dc

    return False
           
cnt = 0
for i in range(m):
    for j in range(n):
        if content[i][j] == '.' and (i, j) != (r, c):
            if good(r, c, i, j):
                cnt += 1
                

print(cnt)

