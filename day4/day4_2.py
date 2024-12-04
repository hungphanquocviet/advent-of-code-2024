filepath = './day4/input.txt'

a = []
with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        a.append(line.strip())

r = len(a)
c = len(a[0])

def search(arr, i, j):
    if i - 1 < 0 or i + 1 >= len(arr) or j - 1 < 0 or j + 1 >= len(arr[0]):
        return 0
    
    tl = arr[i-1][j-1]
    tr = arr[i-1][j+1]
    bl = arr[i+1][j-1]
    br = arr[i+1][j+1]
    
    d1 = tl + arr[i][j] + br
    d2 = tr + arr[i][j] + bl
    
    valid = ["MAS", "SAM"]

    return 1 if d1 in valid and d2 in valid else 0

res = 0
for i in range(r):
    for j in range(c):
        if a[i][j] == 'A':
            res += search(a, i, j)
                
print(res)