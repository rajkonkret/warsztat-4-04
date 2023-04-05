# pliki csv - plik przedzielony znakimm , ; tab
import csv

fields = ["name", "branch", "year", "cgpa"]
row = ["radek", 'COE', '2', '9.1']

my_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Radek', 'year': '3'},
    {'branch': 'COK', 'cgpa': '9', 'name': 'MArek', 'year': '2'},
    {'branch': 'COS', 'cgpa': '8', 'name': 'Kozioł', 'year': '1'},
    {'branch': 'COL', 'cgpa': '9.1', 'name': 'Zając', 'year': '0'}
]

file = 'records.csv'

with open(file, 'w', encoding='utf-8', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)
