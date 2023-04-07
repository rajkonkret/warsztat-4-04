import sqlite3

conn = sqlite3.connect('dane.sqlite')
c = conn.cursor()

# c.execute('''
# CREATE TABLE transakcje
# (data TEXT, id INTEGER, cena REAL)
# ''')

# c.execute('''
# INSERT INTO transakcje VALUES('2023-04-06', 11, 17.50)
# ''')

lista = []
for row in c.execute('SELECT * FROM transakcje ORDER BY cena'):
    # print(row)
    lista.append(row)

conn.commit()
conn.close()

print(lista)
