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
    search = "SELECT last_name, first_name FROM contacts WHERE last_name LIKE '" + input + "%'"
    print(search)
    c.execute(search)
    conn.commit()

def searchByFirst(input):
    search = "SELECT last_name, first_name FROM contacts WHERE first_name LIKE '" + input + "%'"
    c.execute(search)
    conn.commit()

def searchByFull(input_l, input_f):
    WHERE CONCAT(customers.first_name, ' ', customers.last_name) LIKE '%John Smith%'
    search = "SELECT last_name, first_name FROM contacts WHERE CONCAT(first_name, ' ', last_name) LIKE '%" + input_f + " " + input_l "%'"
    c.execute(search)
    conn.commit()




