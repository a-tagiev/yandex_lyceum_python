cnt = 0
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        for d in line.split():
            if d.strip(',!.?:\n').lower() in line:
                cnt += 1
                break
with open("output.txt", "w") as outfile:
    outfile.write(str(cnt))
