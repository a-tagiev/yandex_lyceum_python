a = input().split(' -> ')
ans = []
req = int(input())
for _ in range(req):
    req_bd = input()
    if 0 < a.index(req_bd) < len(a) - 1:
        ans.append((a[a.index(req_bd) - 1:a.index(req_bd) + 2]))
        continue
    if 0 < a.index(req_bd):
        ans.append((a[a.index(req_bd) - 1:a.index(req_bd) + 1]))
        continue
    if a.index(req_bd) < len(a) - 1:
        ans.append((a[a.index(req_bd):a.index(req_bd) + 2]))
for i in ans:
    print(*i, sep=' -> ')
