import random

with open('lines.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

if len(lines) == 0:
    pass
else:
    random_line = random.choice(lines)
    print(random_line.strip())