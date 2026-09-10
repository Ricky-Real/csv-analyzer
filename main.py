import csv

with open("example.csv", "r") as f:
    data = list(csv.DictReader(f))

ages = [int(person["age"]) for person in data]

print(f"Number of records {len(data)}")
print(f"Average age: {sum(ages) / len(ages):.1f}")
print(f"Youngest: {min(ages)}")
print(f"Oldest: {max(ages)}")