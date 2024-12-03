import re
filepath = './day3/input.txt'

a = ''
with open(filepath, encoding='utf8') as file:
    a = ''.join(line.strip() for line in file)
        
pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
tokens = re.findall(r"do\(\)|don't\(\)|mul\(\s*\d+\s*,\s*\d+\s*\)", a)

active = True
res = 0

for token in tokens:
    if token == 'do()':
        active = True
    elif token == 'don\'t()':
        active = False
    else:
        match = pattern.fullmatch(token)
        if active:
            x, y = map(int, match.groups())
            res += x * y
                
print(res)
