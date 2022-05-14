import sqlite3 as sql

def createDB():
    conn = sql.connect('data.db')
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE jokes (
            joke text,
            id text,
            number integer
        )"""
    )
    conn.commit()
    conn.close()

def insetRow(joke, id, number):
    conn = sql.connect('data.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO jokes VALUES ('{joke}', '{id}', {number})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    createTable()
