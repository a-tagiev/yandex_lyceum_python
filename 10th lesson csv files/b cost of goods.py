import csv

arr = []
with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index > 10:
            break
        arr.append((row[0], int(row[1])))
check_1000 = all(item[1] > 1000 for item in arr)
if check_1000:
    print("error")
    exit()
more_useful = []
for i, j in arr:
    if j <= 1000:
        more_useful.append((i, j))
more_useful.sort(key=lambda x: x[1])
s = 0
cnt = 0
budg = 1000
ans = []
for i, j in more_useful:
    while budg >= 0 and cnt <= 10:
        budg -= j
        cnt += 1
        ans.append(i)
print(ans)