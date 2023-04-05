import csv

filename = 'records.csv'

fields = []
rows = []


def read_csv_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as csv_f:
        csvreader = csv.DictReader(csv_f, delimiter=';')

        for row in csvreader:
            yield row


x = read_csv_file(filename)
print(next(x))
for row in read_csv_file(filename):
    rows.append(row)

print(fields)
print(rows)

# 15:00
