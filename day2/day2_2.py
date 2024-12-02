filepath = './day2/sample.txt'

a = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        temp = list(map(int, line.split()))
        a.append(temp)

cnt = 0

def is_safe(code):
    increase = all(code[i] < code[i+1] for i in range(len(code) - 1))
    decrease = all(code[i] > code[i+1] for i in range(len(code) - 1))

    good = True
    for i in range(1, len(code)):
        if abs(code[i] - code[i-1]) > 3 or abs(code[i] - code[i-1]) < 1:
            good = False
            break
    safe = (increase or decrease) and good
    return safe

def check_safety(code):
    if is_safe(code):
        return True
    
    for i in range(len(code)):
        temp = code[:i] + code[i+1:]
        if is_safe(temp):
            return True
    
    return False

for code in a:
    if check_safety(code):
        cnt += 1

print(cnt)
