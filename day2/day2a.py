filepath = './day2/sample.txt'

a = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        temp = list(map(int, line.split()))
        a.append(temp)

cnt = 0

def check_array(arr):
    if all(arr[i] < arr[i+1] for i in range(len(arr) - 1)):
        return "inc"
    elif all(arr[i] > arr[i+1] for i in range(len(arr) - 1)):
        return "dec"
    else:
        return "no"
    
for code in a:
    if check_array(code) == "no":
        continue

    safe = True
    for i in range(1, len(code)):
        if abs(code[i] - code[i-1]) > 3 or abs(code[i] - code[i-1]) < 1:
            safe = False
            break
    if safe:
        cnt += 1

print(cnt)