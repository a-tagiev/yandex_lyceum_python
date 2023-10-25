import csv

minimum = int(input())
ans = []
with open('vps.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        if row[-2].isdigit():
            if int(row[-2]) >= minimum:
                ans.append(row[0])

print(*ans, sep='\n')
