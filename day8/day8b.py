from collections import defaultdict
filepath = './day8/input.txt'

grid = []
with open(filepath, encoding='utf8') as file:
    grid = [line.strip() for line in file.readlines()]

def bound(r, c, i, j):
    return 0 <= i < r and 0 <= j < c

nodes = defaultdict(list)
antinodes = set()

r = len(grid)
c = len(grid[0])
for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            nodes[grid[i][j]].append((i, j))
            antinodes.add((i, j))


for _, node_list in nodes.items():
    for i in range(len(node_list)):
        for j in range(i + 1, len(node_list)):
            scale = 1
            while True:
                x = node_list[i][0] - (node_list[j][0] - node_list[i][0]) * scale
                y = node_list[i][1] - (node_list[j][1] - node_list[i][1]) * scale
                if bound(r, c, x, y):
                    antinodes.add((x, y))
                else:
                    break
                
                scale += 1
                
            scale = 1
            while True:
                x = node_list[j][0] + (node_list[j][0] - node_list[i][0]) * scale
                y = node_list[j][1] + (node_list[j][1] - node_list[i][1]) * scale
                if bound(r, c, x, y):
                    antinodes.add((x, y))
                else:
                    break
                
                scale += 1

print(len(antinodes))            
