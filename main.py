import csv

with open("example.csv", "r") as f:
    data = list(csv.reader(f))

print(f"Number of records {len(data)}")