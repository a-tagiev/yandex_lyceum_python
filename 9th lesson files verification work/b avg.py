import sys

def average(lst):
    if len(lst) == 0:
        return 0.0
    return sum(lst) / len(lst)

def is_numeric(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

district_data = {}
files = []

while True:
    line = input()
    if not line:
        break
    if line[0] == '#':
        current_file = line[1:]
        district_data[current_file] = []
    else:
        walkers = int(line)
        if walkers >= 50:
            district_data[current_file].append(walkers)

with open('hot_may.txt', 'w') as output_file:
    for district, streets in district_data.items():
        if len(streets) > 0:
            avg_value = round(average(streets), 2)
            output_file.write(f"{district}: {avg_value}\n")
