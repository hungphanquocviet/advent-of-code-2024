from collections import defaultdict
filepath = './day8/input.txt'

grid = []
with open(filepath, encoding='utf8') as file:
    grid = [line.strip() for line in file.readlines()]

def bound(r, c, i, j):
    return 0 <= i < r and 0 <= j < c

nodes = defaultdict(list)

r = len(grid)
c = len(grid[0])
for i in range(r):
    for j in range(c):
        if grid[i][j] != ".":
            nodes[grid[i][j]].append((i, j))

antinodes = set()
for _, node_list in nodes.items():
    for i in range(len(node_list)):
        for j in range(i + 1, len(node_list)):
            x = node_list[i][0] - (node_list[j][0] - node_list[i][0])
            y = node_list[i][1] - (node_list[j][1] - node_list[i][1])
            if bound(r, c, x, y):
                antinodes.add((x, y))
            
            x = node_list[j][0] + (node_list[j][0] - node_list[i][0])
            y = node_list[j][1] + (node_list[j][1] - node_list[i][1])
            if bound(r, c, x, y):
                antinodes.add((x, y))

print(len(antinodes))            
