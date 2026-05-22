import csv

total = 0
rows = 0

with open("sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["amount"])
        rows += 1

print(f"Total sales: {total} BDT")
print(f"Number of transactions: {rows}")
print(f"Average sale: {total // rows} BDT")