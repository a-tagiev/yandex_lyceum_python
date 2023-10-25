cnt = 0
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        for w in line.split():
            w_low = w.lower()
            if w_low.startswith("далек"):
                cnt += 1
                break
with open("output.txt", "w") as outfile:
    outfile.write(str(cnt))
