filepath = './day10/input.txt'

grid = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        grid.append([int(c) for c in line.strip()])

def search(grid, i, j, curr, visited):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0
    if (visited[i][j] or grid[i][j] - curr != 1):
        return 0
    
    visited[i][j] = True
    if (grid[i][j] == 9):
        return 1
    
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    ans = 0
    for d in dirs:
        ans += search(grid, i + d[0], j + d[1], grid[i][j], visited)
    
    return ans
    
r = len(grid)
c = len(grid[0])

score = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] == 0:
            visited = [[False] * c for _ in range(r)]
            score += search(grid, i, j, -1, visited)
            
print(score)