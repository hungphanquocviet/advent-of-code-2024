filepath = './day1/input.txt'
a = None

with open(filepath, encoding='utf8') as file:
    a = [line.strip() for line in file.readlines()]
