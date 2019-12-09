import sqlite3

conn = sqlite3.connect('contacts.db')
c = conn.cursor()

def createTable():
    createContactTable = """CREATE TABLE contacts (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                company_name TEXT,
                address TEXT,
                email TEXT,
                phone TEXT
                )"""
    c.execute(createContactTable)
    conn.commit()

def searchByLast(input):
    search = "SELECT last_name, first_name FROM contacts WHERE last_name LIKE" + input + "%'"
    c.execute(search)
    conn.commit()





