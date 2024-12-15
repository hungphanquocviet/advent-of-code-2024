filepath = './day11/input.txt'

stones = None
with open(filepath, encoding='utf8') as file:
    stones = file.readline().strip().split()

blinks = 25
for _ in range(blinks):
    i = 0
    while i < len(stones):
        if stones[i] == '0':
            stones[i] = '1'
        
        elif len(stones[i]) % 2 == 0:
            temp = stones[i]
            stones[i] = str(int(temp[:len(temp)//2]))
            stones.insert(i+1, str(int(temp[len(temp)//2:])))
            i += 1
        
        else:
            stones[i] = str(int(stones[i]) * 2024)
        
        i += 1

print(len(stones))