a = int(input())
dots_0 = []
dict = {'I': 0, 'II': 0, 'III': 0, 'IV': 0}
for _ in range(a):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        dots_0.append((x, y))
        continue
    if x > 0:
        if y > 0:
            dict['I'] += 1
            continue
        dict['IV'] += 1
    if x < 0:
        if y > 0:
            dict['II'] += 1
            continue
        dict['III'] += 1
if dots_0:
    print(*dots_0, sep='\n')
print(str(dict).strip('{}').replace("'", "") + '.')
