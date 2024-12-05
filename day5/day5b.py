from collections import defaultdict, deque

def good(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    for u in graph:
        for v in graph[u]:
            if u in position and v in position:  
                if position[u] > position[v]:
                    return False
    return True

def topo_sort(update, graph):
    subgraph = {page: [] for page in update}
    in_deg = {page: 0 for page in update}
    
    for u in graph:
        for v in graph[u]:
            if u in update and v in update:
                subgraph[u].append(v)
                in_deg[v] += 1
    
    queue = deque([page for page in update if in_deg[page] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in subgraph[current]:
            in_deg[neighbor] -= 1
            if in_deg[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

filepath = './day5/input.txt'

content = ''
with open(filepath, encoding='utf8') as file:
    content = file.read()
    
sections = content.strip().split('\n\n')
rules_raw = sections[0].splitlines()
updates_raw = sections[1].splitlines()

rules = [rule.strip() for rule in rules_raw]
updates = [list(map(int, update.strip().split(','))) for update in updates_raw]

graph = defaultdict(list)
for rule in rules:
    x, y = map(int, rule.split('|'))
    graph[x].append(y)
    
invalid = []
for update in updates:
    if not good(update, graph):
        invalid.append(update)

corrected = [topo_sort(update, graph) for update in invalid]
mid_eles = [vals[len(vals)//2] for vals in corrected]
res = sum(mid_eles)
print(res)