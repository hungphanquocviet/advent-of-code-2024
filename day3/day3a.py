import re
filepath = './day3/input.txt'

a = ''
with open(filepath, encoding='utf8') as file:
    a = ''.join(line.strip() for line in file)

pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')
tokens = re.findall(r"mul\(\s*\d+\s*,\s*\d+\s*\)", a)

res = 0
for token in tokens:
    match = pattern.fullmatch(token)
    x, y = map(int, match.groups())
    res += x * y

print(res)


