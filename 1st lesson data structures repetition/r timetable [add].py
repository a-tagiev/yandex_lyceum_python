classrooms = {}
day = input()
while day:
    line = input()
    while line:
        subject, room = line.split()
        room = int(room)
        if room not in classrooms:
            classrooms[room] = []
        classrooms[room].append(subject)
        line = input()
    day = input()

st = sorted(classrooms.items())

for room, subjects in st:
    subject_list = ", ".join(set(subjects))
    print(f"{room}: {subject_list}")
