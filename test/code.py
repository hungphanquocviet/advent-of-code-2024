filepath = './test/input.txt'
a = None

with open(filepath, encoding='utf8') as file:
    a = [line.strip() for line in file.readlines()]

res = 0

for s in a:
    a, b = None, None
    for i in range(len(s)):
        if s[i].isdigit():
            a = s[i]
            break
    
    for i in range(len(s)-1, -1, -1):
        if s[i].isdigit():
            b = s[i]
            break
    
    combine = a + b
    res += int(combine)

print(res)

   
