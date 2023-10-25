cnt = 0

with open("input.txt", "r") as file:
    for i in file:
        scene_lower = i.lower()
        if 'далек' in scene_lower:
            cnt += 1
with open("output.txt", "w") as outfile:
    outfile.write(str(cnt))
