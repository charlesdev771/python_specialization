import sqlite3

class Simple_Agenda:

    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, tel):
        consult =  'INSERT INTO agenda (name, tel) VALUES (?,?)'
        self.cursor.execute(consult, (name, tel))
        self.conn.commit()

    def edit(self, name, tel, id):
        consult = 'UPDATE agenda SET name=?, tel=? WHERE id=?'
        self.cursor.execute(consult, (name, tel, id))
        self.conn.commit()

    def remove(self, id):
        consult = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute('SELECT * FROM agenda')
        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = Simple_Agenda('agenda.db')
    agenda.insert('Charles', '777')
