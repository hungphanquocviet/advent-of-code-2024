import math
filepath = './day1/sample.txt'

a = []

with open(filepath, encoding='utf8') as file:
    for line in file.readlines():
        x, y = map(int, line.strip().split())

