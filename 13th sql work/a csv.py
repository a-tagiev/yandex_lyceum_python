import csv
import math

min_toska = int(input())


def calculate_toska(entertainments, distance_to_bukhara):
    toska = math.floor((entertainments / distance_to_bukhara) * 100)
    return toska


with open("main_cities.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='.')
    print(reader.fieldnames[1], "(toska)")
    for row in reader:
        city = row['city']
        entertainments = int(row['entertainments'])
        distance_to_bukhara = int(row['distance'])
        toska = calculate_toska(entertainments, distance_to_bukhara)
        if toska >= min_toska:
            print(f"{city} ({toska})")
