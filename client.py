import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def createTable():
    createContactTable = """CREATE TABLE contacts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER
                name TEXT,
                email TEXT,
                phone INTEGER
                )"""
    c.execute(createContactTable)
    conn.commit()


