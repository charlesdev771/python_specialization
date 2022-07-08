import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clientes ( '

    'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    'name TEXT,'
    'peso REAL'
')')

cursor.execute('INSERT INTO clientes (name, peso) VALUES (?, ?)', ('Charles2', 20))

cursor.execute('INSERT INTO clientes (name, peso) VALUES (:name, :peso)',
    {'name': 'AA', 'peso': 50}
)

conn.commit()

cursor.execute('SELECT * FROM clientes')
for line in cursor.fetchall():
    indentificador, name, peso = line
    print(indentificador, name, peso)

cursor.execute('UPDATE clientes SET name = :name WHERE id=:id',  {'name': 'Paula', 'id': 2})
conn.commit()

cursor.execute('SELECT * FROM clientes')
for line in cursor.fetchall():
    indentificador, name, peso = line
    print(indentificador, name, peso)

cursor.close()
conn.close()
