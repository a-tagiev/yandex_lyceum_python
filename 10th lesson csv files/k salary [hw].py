import csv

fl = 0
ans = []
with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        fl += 1
        if fl == 1:
            continue
        if int(row[-2]) > int(row[-1]):
            ans.append(row[0])

with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    # Записываем данные в файл
    for row in data:
        writer.writerow(row)
