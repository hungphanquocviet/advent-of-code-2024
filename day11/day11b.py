from functools import lru_cache

filepath = './day11/input.txt'

stones = None
with open(filepath, encoding='utf8') as file:
    stones = file.readline().strip().split()

blinks = 75

@lru_cache(maxsize=None)
def count_stones(stone, blinks):
    if blinks == 0:
        return 1

    if stone == '0':
        return count_stones('1', blinks - 1)
    
    elif len(stone) % 2 == 0:
        l = str(int(stone[:len(stone) // 2]))
        r = str(int(stone[len(stone) // 2:]))
        
        return count_stones(l, blinks - 1) + count_stones(r, blinks - 1)
        
    else:
        return count_stones(str(int(stone) * 2024), blinks - 1)
    
res = sum([count_stones(stone, blinks) for stone in stones])
print(res)