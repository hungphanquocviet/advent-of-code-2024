from collections import defaultdict
filepath = './day5/input.txt'

content = ''
with open(filepath, encoding='utf8') as file:
    content = file.read()

def good(update, graph):
    position = {page: idx for idx, page in enumerate(update)}
    for u in graph:
        for v in graph[u]:
            if u in position and v in position:  
                if position[u] > position[v]:
                    return False
    return True

sections = content.strip().split('\n\n')
rules_raw = sections[0].splitlines()
updates_raw = sections[1].splitlines()

rules = [rule.strip() for rule in rules_raw]
updates = [list(map(int, update.strip().split(','))) for update in updates_raw]

graph = defaultdict(list)
for rule in rules:
    x, y = map(int, rule.split('|'))
    graph[x].append(y)
    
valid = []
for update in updates:
    if good(update, graph):
        valid.append(update)

mid_eles = [vals[len(vals)//2] for vals in valid]
res = sum(mid_eles)
print(res)